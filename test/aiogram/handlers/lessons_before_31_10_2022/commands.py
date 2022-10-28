from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=["commands"])
async def commands(message: types.Message):
    await message.answer("Test commands")