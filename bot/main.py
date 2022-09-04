import traceback, time, config, json
from datetime import date as dt
from datetime import time as tm
from admin import *
import telebot as tg

bot = tg.TeleBot(config.token)

users = load_json('jsons/users.json')
lessons = load_json('jsons/lessons.json')

#=====================================================SHORT  NAMES=====================================================#

reply = bot.reply_to
send = bot.send_message

def get_day(week_num, day):
    for t in lessons[str(week_num)]:
        res = t[str(day)]
    return ''.join(res)

hel = ['help', 'хелп']
tom = ['tomorrow', 'завтра', 'Завтра']
tod = ['today', 'сегодня', 'Сегодня']
yest = ['yesterday', 'вчера', 'Вчера']
calls = ['calls', 'звонки']
full = ['full', 'Фулл расписание', 'фулл расписание', 'Фулл', 'фулл']
c1 = ['Нечетная', 'нечетная', 'odd']
c2 = ['Четная', 'четная', 'even']
nxt = ['Следующая неделя', 'следующая неделя', 'next']

#============================================ALL COMMANDS FOR SEND MESSAGES============================================#

@bot.message_handler(commands=['start'])
def send_welcome(message):
    reply(message, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать тебе ориентироваться по предметам в течении дня. Напиши /help для того, чтобы узнать мои возможности".format(message.from_user, bot.get_me()), parse_mode='html')
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_name = message.from_user.username

    users[str(message.from_user.id)] = [
        {
            "us_name": str(user_first_name) + str(user_last_name),
            "us_username": str(user_name),
            "us_id": str(user_id),
            "us_reg": int(0)
        }]
    write_json('jsons/users.json', users)

@bot.message_handler(commands=hel)
def send_help(message):
    reply(message, f'''
    Мои команды:
    /вчера - расписание на вчерашний день
    /сегодня - расписание на сегодня
    /завтра - расписание на завтра
    /звонки - расписание звонков и перемен
    /фулл расписание
    /четная - расписание четной недели
    /нечетная - расписание нечетной недели
    /следующая - расписание следующей недели
    ''' )

@bot.message_handler(commands=tod)
def send_today(message):
    today = dt.today().weekday()
    week_now = dt.today().isocalendar().week
    yesterday = today - 1
    tomorrow = today + 1

    if tomorrow >= 7: 
        tomorrow = 0
        week_now = week_now + 1
    if yesterday < 0: yesterday = 0

    if week_now % 2 == 0: reply(message, get_day("четная", today))
    else: reply(message, get_day("нечетная", today))

@bot.message_handler(commands=tom)
def send_tomorrow(message):
    today = dt.today().weekday()
    week_now = dt.today().isocalendar().week
    yesterday = today - 1
    tomorrow = today + 1

    if tomorrow >= 7: 
        tomorrow = 0
        week_now = week_now + 1
    if yesterday < 0: yesterday = 0
    
    if week_now % 2 == 0: reply(message, get_day("четная", tomorrow))
    else: reply(message, get_day("нечетная", tomorrow))

@bot.message_handler(commands=yest)
def send_yesterday(message):
    today = dt.today().weekday()
    week_now = dt.today().isocalendar().week
    yesterday = today - 1
    tomorrow = today + 1

    if tomorrow >= 7: 
        tomorrow = 0
        week_now = week_now + 1
    if yesterday < 0: yesterday = 0
    
    if week_now % 2 == 0: reply(message, get_day("четная", yesterday))
    else: reply(message, get_day("нечетная", yesterday))

@bot.message_handler(commands=calls)
def send_call(message):
    reply(message, ''.join(lessons["звонки"]))

@bot.message_handler(commands=full)
def send_full(message):
    reply(message, full_1)
    reply(message, full_2)

@bot.message_handler(commands=c1)
def send_odd(message):
    reply(message, full_2)

@bot.message_handler(commands=c2)
def send_even(message):
    reply(message, full_1)

@bot.message_handler(commands=nxt)
def send_nxt(message):
    week_now = dt.today().isocalendar().week
    
    if week_now % 2 == 0: reply(message, full_2)
    else: reply(message, full_1)
    


#======================================================================================================================#
def telegram_polling():
    try:
        bot.polling()
    except:
        traceback_error_string = traceback.format_exc()
        with open("Error.log", "a") as myfile:
            myfile.write(time.strftime("%c") + "\r\n<<START ERROR polling>>\r\n" + traceback_error_string + "\r\n<<END ERROR polling>>" + "\r\n\r\n")
        bot.stop_polling()
        time.sleep(10)
        telegram_polling()

telegram_polling()
# bot.polling()