from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *
from utils.week_counter import *


@dp.message_handler(commands=full)
async def full_week(message: types.Message):
    await message.answer(even_week)
    await message.answer(odd_week)