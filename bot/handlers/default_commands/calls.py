from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=callss)
async def calls(message: types.Message):
    await message.answer(''.join(calls_json["звонки"]))