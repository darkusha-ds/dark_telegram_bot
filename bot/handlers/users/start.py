from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=start)
async def start(message: types.Message):
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}!\nЯ - бот созданный чтобы помогать тебе ориентироваться по предметам в течении дня.", parse_mode='html', reply_markup=welcome_key)

    reg_users(message)