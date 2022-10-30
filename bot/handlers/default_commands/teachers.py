from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=teachers)
async def teachers(message: types.Message):
    await message.answer("Выберите нужного преподавателя из списка", reply_markup=teachers_key)