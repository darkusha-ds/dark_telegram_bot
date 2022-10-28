from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=cher4enie)
async def cher4enie(message: types.Message):
    await message.answer(get_teacher(str(g_cher4enie), 0))
    await message.answer(get_teacher(str(g_cher4enie), 1))
    await message.answer(get_teacher(str(g_cher4enie), 2))