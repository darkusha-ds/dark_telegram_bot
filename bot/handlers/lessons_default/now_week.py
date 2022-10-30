from aiogram import types
from datetime import datetime as dt

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *
from utils.week_counter import *


@dp.message_handler(commands=nw)
async def now_week(message: types.Message):
    week_now = dt.today().isocalendar().week

    if week_now % 2 == 0: await message.answer(even_week)
    else: await message.answer(odd_week)