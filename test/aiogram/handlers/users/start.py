from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=start)
async def start(message: types.Message):
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}!\nЯ - бот созданный чтобы помогать тебе ориентироваться по предметам в течении дня.", parse_mode='html', reply_markup=welcome_key)

    users[str(message.from_user.id)] = [
        {
            "us_name": str(message.from_user.first_name) + str(message.from_user.last_name),
            "us_username": str(message.from_user.username),
            "us_id": str(message.from_user.id)
        }]
    write_json('data/jsons/users.json', users)