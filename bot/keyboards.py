from telebot import *
from phrazes import *

welcome_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
welcome0  = types.KeyboardButton('/рестарт')
welcome1 = types.KeyboardButton('/gif')
welcome2 = types.KeyboardButton('/преподы')
welcome3  = types.KeyboardButton('/сегодня')
welcome4  = types.KeyboardButton('/завтра')
welcome5  = types.KeyboardButton('/вчера')
welcome6  = types.KeyboardButton('/звонки')
welcome7  = types.KeyboardButton('/фулл расписание')
welcome8  = types.KeyboardButton('/нечетная')
welcome9  = types.KeyboardButton('/четная')
welcome10  = types.KeyboardButton('/next')
welcome11 = types.KeyboardButton('/now')

welcome_key.add(welcome0, welcome1, welcome2, welcome3, welcome4, welcome5, welcome6, welcome7, welcome8, welcome9, welcome10, welcome11)


teachers_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
teachers0 = types.KeyboardButton('/{}'.format(bk))
teachers1 = types.KeyboardButton('/{}'.format(math))
teachers2 = types.KeyboardButton('/{}'.format(cher4enie))
teachers3 = types.KeyboardButton('/{}'.format(fizra))
teachers4 = types.KeyboardButton('/{}'.format(management))
teachers5 = types.KeyboardButton('/{}'.format(history))
teachers6 = types.KeyboardButton('/{}'.format(english))
teachers7 = types.KeyboardButton('/{}'.format(informatika))
teachers_key.add(teachers0, teachers1, teachers2, teachers3, teachers4, teachers5, teachers6, teachers7)