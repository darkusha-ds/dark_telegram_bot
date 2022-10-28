from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=back)
async def back(message: types.Message):
    await message.answer('Вы вернулись в главное меню', reply_markup=welcome_key)