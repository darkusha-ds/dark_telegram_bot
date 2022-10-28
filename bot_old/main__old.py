import traceback, time, config
from datetime import date as dt
from admin import *
import telebot as tg
from keyboards import *

bot = tg.TeleBot(config.token)

users = load_json('jsons/users.json')
lessons = load_json('jsons/lessons.json')
lessons_1 = load_json('jsons/lessons_new.json')
teacher = load_json('jsons/teachers.json')

#=====================================================SHORT  NAMES=====================================================#

reply = bot.reply_to
send = bot.send_message

def get_day(week_num, day):
    for t in lessons[str(week_num)]:
        res = t[str(day)]
    return ''.join(res)

#============================================ALL COMMANDS FOR SEND MESSAGES============================================#

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