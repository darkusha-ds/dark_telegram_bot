import traceback, config, time, json, sys
from datetime import date as dt
from datetime import time as tm
from admin import data, adm10, adm11
import telebot as tg

bot = tg.TeleBot(config.token_test)

#=====================================================SHORT  NAMES=====================================================#
today = dt.today().weekday()
yesterday = today - 1
tomorrow = today + 1

reply = bot.reply_to
send = bot.send_message
#======================================================================================================================#
def get_time_table_today(cls_num, day='today'):
    for t in data[str(cls_num)]:
        res = t[str(today)]
    return ''.join(res)

def get_time_table_tomorrow(cls_num, day='tomorrow'):
    for t in data[str(cls_num)]:
        res = t[str(tomorrow)]
    return ''.join(res)

lesson = ''.join(data["lessons"])
#============================================ALL COMMANDS FOR SEND MESSAGES============================================#
@bot.message_handler(commands=['start'])
def send_welcome(message):
    reply(message, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать тебе ориентироваться по предметам в течении дня. Напиши /help для того, чтобы узнать мои возможности".format(message.from_user, bot.get_me()), parse_mode='html')

@bot.message_handler(commands=['help'])
def send_help(message):
    reply(message, f'Мои команды: \n \n' + '10 - расписание 10-го класса \n' + '11 - расписание 11-го класса \n' + 'завтра 10 - посмотреть расписание 10-х на завтра \n' + 'завтра 11 - посмотреть расписание 11-х на завтра \n' + "уроки - время уроков" )

@bot.message_handler(content_types=['text'])
def send_text(message):
    lowwer = message.text.lower()
    mci = message.chat.id
    if lowwer == '10':
        send(mci, get_time_table_today(10))
    elif lowwer == 'завтра 10':
        if today == 4: reply(message, 'Завтра суббота')
        elif today == 5: reply(message, 'Завтра воскресенье')
        else: send(mci, get_time_table_tomorrow(10))

    elif lowwer == '11':
        send(mci, get_time_table_today(11))
    elif lowwer == 'завтра 11':
        if today == 4: reply(message, 'Завтра суббота')
        elif today == 5: reply(message, 'Завтра воскресенье')
        else: send(mci, get_time_table_tomorrow(11))

    elif lowwer == 'admin 10':
        send(mci, adm10)
    elif lowwer == 'admin 11':
        send(mci, adm11)

    elif lowwer == 'уроки':
        send(mci, lesson)

    else:
        reply(message, 'Error')

#======================================================================================================================#
def telegram_polling():
    try:
        bot.polling()
    except:
        traceback_error_string = traceback.format_exc()
        with open("Error.log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c") + "\r\n<<START ERROR polling>>\r\n" + traceback_error_string + "\r\n<<END ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

telegram_polling()