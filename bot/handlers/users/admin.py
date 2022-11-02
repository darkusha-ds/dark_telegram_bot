from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    if str(message.from_user.id) in ["1453000194", "411175364"]:
        await message.answer(users)
        return
    await message.answer("Извините, вы не создатель данного бота")