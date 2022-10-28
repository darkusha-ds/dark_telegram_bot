from aiogram import types
from datetime import date as dt

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=["yesterday"])
async def yesterday(message: types.Message):
    today = dt.today().weekday()
    week_now = dt.today().isocalendar().week
    yesterday = today - 1
    tomorrow = today + 1
 
    if tomorrow >= 7: 
        tomorrow = 0
        week_now = week_now + 1
    if yesterday < 0: yesterday = 0

    if week_now % 2 == 0:  await message.answer(get_day_default("четная", yesterday))
    else: await message.answer(get_day_default("нечетная", yesterday))