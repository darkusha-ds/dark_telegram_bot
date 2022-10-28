from aiogram import *

from utils.phrazes import *

welcome_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
welcome_0  = types.KeyboardButton('/рестарт')
welcome_1 = types.KeyboardButton('/gif')
welcome_2 = types.KeyboardButton('/преподы')
welcome_3  = types.KeyboardButton('/сегодня')
welcome_4  = types.KeyboardButton('/завтра')
welcome_5  = types.KeyboardButton('/вчера')
welcome_6  = types.KeyboardButton('/звонки')
welcome_7  = types.KeyboardButton('/фулл расписание')
welcome_8  = types.KeyboardButton('/нечетная')
welcome_9  = types.KeyboardButton('/четная')
welcome_10  = types.KeyboardButton('/next')
welcome_11 = types.KeyboardButton('/now')

welcome_key.add(
    welcome_0,
    welcome_1, 
    welcome_2, 
    welcome_3, 
    welcome_4, 
    welcome_5, 
    welcome_6, 
    # welcome_7, 
    # welcome_8, 
    # welcome_9, 
    # welcome_10,
    # welcome_11
)


teachers_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
teachers_0 = types.KeyboardButton('/{}'.format(g_back))
teachers_1 = types.KeyboardButton('/{}'.format(g_math))
teachers_2 = types.KeyboardButton('/{}'.format(g_cher4enie))
teachers_3 = types.KeyboardButton('/{}'.format(g_fizra))
teachers_4 = types.KeyboardButton('/{}'.format(g_management))
teachers_5 = types.KeyboardButton('/{}'.format(g_history))
teachers_6 = types.KeyboardButton('/{}'.format(g_english))
teachers_7 = types.KeyboardButton('/{}'.format(g_informatika))

teachers_key.add(
    teachers_0, 
    teachers_1, 
    teachers_2, 
    teachers_3, 
    teachers_4, 
    teachers_5, 
    teachers_6, 
    teachers_7
)

new_week_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
new_week_0 = types.KeyboardButton('/рестарт')
new_week_00 = types.KeyboardButton('/{}'.format(g_back))
new_week_1 = types.KeyboardButton('/сегодня')
new_week_2 = types.KeyboardButton('/завтра')
new_week_3 = types.KeyboardButton('/вчера')
new_week_4 = types.KeyboardButton('/звонки')
new_week_5 = types.KeyboardButton('/фулл расписание')
new_week_6 = types.KeyboardButton('/нечетная')
new_week_7 = types.KeyboardButton('/четная')
new_week_8 = types.KeyboardButton('/next')
new_week_9 = types.KeyboardButton('/now')

new_week_key.add(
    new_week_0,
    new_week_00,
    new_week_1,
    new_week_2,
    new_week_3,
    new_week_4,
    new_week_5,
    new_week_6,
    new_week_7,
    new_week_8,
    new_week_9
)