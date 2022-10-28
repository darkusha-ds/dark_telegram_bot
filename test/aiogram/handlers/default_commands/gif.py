from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=gif)
async def gif(message: types.Message):
    await message.answer_animation(types.InputFile('media/MTID.mp4'))