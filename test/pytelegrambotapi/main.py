import traceback, time, config, json
from datetime import date as dt
from datetime import time as tm
from admin import *
import telebot as tg

bot = tg.TeleBot(config.token)

class user:
    def __init__(self, name, cl, id):
        self.name = name
        self.cl = cl
        self.id = id

users = load_json('jsons/users.json')

#=====================================================SHORT  NAMES=====================================================#

today = dt.today().weekday()
yesterday = today - 1
tomorrow = today + 1

reply = bot.reply_to
send = bot.send_message
next_step = bot.register_next_step_handler

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
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_name = message.from_user.username
    
    users[str(user_id)] = []

    users[str(user_id)].append(str(message.from_user.id))

    # users[str(message.from_user.id)] = [
    #     {
    #         "us_name": str(user_first_name) +str(user_last_name),
    #         "us_username": str(user_name),
    #         "us_id": str(user_id),
    #         "us_reg": int(0)
    #     }]
    write_json('jsons/users.json', users)

# def check(current_id): # функция которая проверяет зарегистрирован ли человек
#     for i in users[str(current_id)][0]["us_reg"]:
#         if i == 0:
#             return 1
#     return 0

#=====================================================REGISTRATION=====================================================#
# @bot.message_handler(commands=["reg"])
# def other_name(message):
#     global user_id #глобальная переменная хранящая id зарегистрировшегося пользователя
#     user_id = message.from_user.id # принятие информации из текста, который отправляет пользователь
#     # if check(user_id) == 1: #если такой id уже зарегистрирован, то не дает зарегистрироваться второй раз
#     #     reply(message, f"Ошибка, ты уже прошел регистрацию")
#     # else:
#     reply(message, f"Пожалуйста введи свое имя и фамилию.\nНо учитывай, что данные будут проверяться, если будет какая-то проблема, то вы будете заблокированы до выяснения вашей личности!")
#     next_step(message, get_name)  # переход к следующей функции

# def get_name(message):
#     global name
#     name = message.text.lower() #функция, которая узнает имя пользователя
#     reply(message, f"Теперь напиши свой класс (вместе с буквой)")
#     next_step(message, get_class)

# def get_class(message):
#     global cl
#     cl = message.text.lower()
#     if (cl == '10а') or (cl == '10б') or (cl == '10в') or (cl == '11а') or (cl == '11б') or (cl == '11в') or (cl == '11a') or (cl == '11b') or (cl == '11c'):
#         users[str(message.from_user.id)][0]["us_name"].append(str(name))
#         users[str(message.from_user.id)][0]["us_grate"].append(str(cl))
#         users[str(message.from_user.id)][0]["us_id"].append(str(user_id))
#         write_json('jsons/users.json', users)
#         reply(message, f"Ты зарегистрирован в моей базе данных. Приятного пользования")
#     else:
#         reply(message, f"Ошибка, в моем списке есть только старшие классы\nРегистрация не пройдена, пройди её заново с помощью команды /reg")

#===================================================END REGISTRATION===================================================#

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
        if today == 4:
            reply(message, 'Завтра суббота')
        elif today == 5:
            reply(message, 'Завтра воскресенье')
        else:
            send(mci, get_time_table_tomorrow(10))

    elif lowwer == '11':
        send(mci, get_time_table_today(11))
    elif lowwer == 'завтра 11':
        if today == 4:
            reply(message, 'Завтра суббота')
        elif today == 5:
            reply(message, 'Завтра воскресенье')
        else:
            send(mci, get_time_table_tomorrow(11))

    elif lowwer == 'admin 10':
        send(mci, adm10)
    elif lowwer == 'admin 11':
        send(mci, adm11)

    elif lowwer == 'уроки':
        send(mci, lesson)

    else:
        reply(message, 'Error')

#======================================================================================================================#
# def telegram_polling():
#     try:
#         bot.polling()
#     except:
#         traceback_error_string = traceback.format_exc()
#         with open("Error.log", "a") as myfile:
#             myfile.write(time.strftime("%c") + "\r\n<<START ERROR polling>>\r\n" + traceback_error_string + "\r\n<<END ERROR polling>>" + "\r\n\r\n")
#         bot.stop_polling()
#         time.sleep(10)
#         telegram_polling()

# telegram_polling()
bot.polling()