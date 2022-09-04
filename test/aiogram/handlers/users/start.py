from aiogram import types

from loader import dp


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}!\nЯ - <b>Dark Bot</b>, бот созданный чтобы помогать тебе ориентироваться по предметам в течении дня. Напиши /help для того, чтобы узнать мои возможности", parse_mode='html')