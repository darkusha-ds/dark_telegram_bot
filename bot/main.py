import traceback, time, config, json
from datetime import date as dt
from datetime import time as tm
from admin import *
import telebot as tg
from telebot import *
from phrazes import *
from keyboards import *

bot = tg.TeleBot(config.token)

users = load_json('jsons/users.json')
lessons = load_json('jsons/lessons.json')
teacher = load_json('jsons/teachers.json')

#=====================================================SHORT  NAMES=====================================================#

reply = bot.reply_to
send = bot.send_message

def get_day(week_num, day):
    for t in lessons[str(week_num)]:
        res = t[str(day)]
    return ''.join(res)

def get_fio(subject, num):
    return teacher[str(subject)][num]["ФИО"]

def get_phone(subject, num):
    return teacher[str(subject)][num]["Номер телефона"]

def get_email(subject, num):
    return teacher[str(subject)][num]["email"]

def get_vk(subject, num):
    return teacher[str(subject)][num]["VK"]

#============================================ALL COMMANDS FOR SEND MESSAGES============================================#

@bot.message_handler(commands=st)
def send_welcome(ctx):

    reply(ctx, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помогать тебе ориентироваться по предметам в течении дня.".format(ctx.from_user, bot.get_me()), parse_mode='html', reply_markup=welcome_key)

    users[str(ctx.from_user.id)] = [
        {
            "us_name": str(ctx.from_user.first_name) + str(ctx.from_user.last_name),
            "us_username": str(ctx.from_user.username),
            "us_id": str(ctx.from_user.id),
            "us_reg": int(0)
        }]
    write_json('jsons/users.json', users)

@bot.message_handler(commands=gif)
def send_gif(ctx):
    bot.send_animation(ctx.chat.id, animation=open('media/MTID.mp4', 'rb'))

@bot.message_handler(commands=hel)
def send_help(ctx):
    reply(ctx, f'''
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
def send_today(ctx):
    today = dt.today().weekday()
    week_now = dt.today().isocalendar().week
    yesterday = today - 1
    tomorrow = today + 1

    if tomorrow >= 7: 
        tomorrow = 0
        week_now = week_now + 1
    if yesterday < 0: yesterday = 0

    if week_now % 2 == 0: reply(ctx, get_day("четная", today))
    else: reply(ctx, get_day("нечетная", today))

@bot.message_handler(commands=tom)
def send_tomorrow(ctx):
    today = dt.today().weekday()
    week_now = dt.today().isocalendar().week
    yesterday = today - 1
    tomorrow = today + 1

    if tomorrow >= 7: 
        tomorrow = 0
        week_now = week_now + 1
    if yesterday < 0: yesterday = 0
    
    if week_now % 2 == 0: reply(ctx, get_day("четная", tomorrow))
    else: reply(ctx, get_day("нечетная", tomorrow))

@bot.message_handler(commands=yest)
def send_yesterday(ctx):
    today = dt.today().weekday()
    week_now = dt.today().isocalendar().week
    yesterday = today - 1
    tomorrow = today + 1

    if tomorrow >= 7: 
        tomorrow = 0
        week_now = week_now + 1
    if yesterday < 0: yesterday = 0
    
    if week_now % 2 == 0: reply(ctx, get_day("четная", yesterday))
    else: reply(ctx, get_day("нечетная", yesterday))

@bot.message_handler(commands=calls)
def send_call(ctx):
    reply(ctx, ''.join(lessons["звонки"]))

@bot.message_handler(commands=full)
def send_full(ctx):
    reply(ctx, full_1)
    reply(ctx, full_2)

@bot.message_handler(commands=c1)
def send_odd(ctx):
    reply(ctx, full_2)

@bot.message_handler(commands=c2)
def send_even(ctx):
    reply(ctx, full_1)

@bot.message_handler(commands=nxt)
def send_nxt(ctx):
    week_now = dt.today().isocalendar().week
    
    if week_now % 2 == 0: reply(ctx, full_2)
    else: reply(ctx, full_1)
    
@bot.message_handler(commands=nw)
def send_now(ctx):
    week_now = dt.today().isocalendar().week
    
    if week_now % 2 == 0: reply(ctx, full_1)
    else: reply(ctx, full_2)

@bot.message_handler(commands=back)
def send_back(ctx):
    reply(ctx, 'Вы вернулись в главное меню', reply_markup=welcome_key)

@bot.message_handler(commands=teachers)
def sent_teach_mass(ctx):
    send(ctx.chat.id, "Выберите нужного преподавателя из списка", reply_markup=teachers_key)

@bot.message_handler(commands=math)
def sent_math(ctx):
    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_math, 
        get_fio(str(g_math), 0), 
        get_phone(str(g_math), 0), 
        get_email(str(g_math), 0), 
        get_vk(str(g_math), 0)
        ))
    
@bot.message_handler(commands=cher4enie)
def sent_cher(ctx):
    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_cher4enie, 
        get_fio(str(g_cher4enie), 0), 
        get_phone(str(g_cher4enie), 0), 
        get_email(str(g_cher4enie), 0), 
        get_vk(str(g_cher4enie), 0)
        ))

    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_cher4enie, 
        get_fio(str(g_cher4enie), 1), 
        get_phone(str(g_cher4enie), 1), 
        get_email(str(g_cher4enie), 1), 
        get_vk(str(g_cher4enie), 1)
        ))

    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_cher4enie, 
        get_fio(str(g_cher4enie), 2), 
        get_phone(str(g_cher4enie), 2), 
        get_email(str(g_cher4enie), 2), 
        get_vk(str(g_cher4enie), 2)
        ))
    
@bot.message_handler(commands=fizra)
def sent_fizra(ctx):
    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_fizra, 
        get_fio(str(g_fizra), 0), 
        get_phone(str(g_fizra), 0), 
        get_email(str(g_fizra), 0), 
        get_vk(str(g_fizra), 0)
        ))

    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_fizra, 
        get_fio(str(g_fizra), 1), 
        get_phone(str(g_fizra), 1), 
        get_email(str(g_fizra), 1), 
        get_vk(str(g_fizra), 1)
        ))
    
@bot.message_handler(commands=management)
def sent_management(ctx):
    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_management, 
        get_fio(str(g_management), 0), 
        get_phone(str(g_management), 0), 
        get_email(str(g_management), 0), 
        get_vk(str(g_management), 0)
        ))
    
@bot.message_handler(commands=history)
def sent_history(ctx):
    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_history, 
        get_fio(str(g_history), 0), 
        get_phone(str(g_history), 0), 
        get_email(str(g_history), 0), 
        get_vk(str(g_history), 0)
        ))
    
@bot.message_handler(commands=english)
def sent_english(ctx):
    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_english, 
        get_fio(str(g_english), 0), 
        get_phone(str(g_english), 0), 
        get_email(str(g_english), 0), 
        get_vk(str(g_english), 0)
        ))

    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_english, 
        get_fio(str(g_english), 1), 
        get_phone(str(g_english), 1), 
        get_email(str(g_english), 1), 
        get_vk(str(g_english), 1)
        ))
    
@bot.message_handler(commands=informatika)
def sent_informatika(ctx):
    send(ctx.chat.id, "{0}\n\nФИО: {1}\nНомер телефона: {2}\nemail: {3}\nVK: {4}".format(\
        g_informatika, 
        get_fio(str(g_informatika), 0), 
        get_phone(str(g_informatika), 0), 
        get_email(str(g_informatika), 0), 
        get_vk(str(g_informatika), 0)
        ))

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