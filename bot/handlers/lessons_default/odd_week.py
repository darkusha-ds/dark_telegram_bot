from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *
from utils.week_counter import *


@dp.message_handler(commands=c1)
async def odd_week_s(message: types.Message):
    await message.answer(odd_week)