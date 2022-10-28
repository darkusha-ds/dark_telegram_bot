from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=management)
async def management(message: types.Message):
    await message.answer(get_teacher(str(g_management), 0))