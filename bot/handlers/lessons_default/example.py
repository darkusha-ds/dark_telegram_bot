from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=example)
async def example(message: types.Message):
    await message.answer('adklf')