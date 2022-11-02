from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=informatika)
async def informatika(message: types.Message):
    if str(message.from_user.id) in block_user["blocked"]:
        await message.answer("Извините, вы находитесь в черном списке. Если вы считаете что попали туда ошибочно, напишите создателю: @darkusha_ds")
        return
    await message.answer(get_teacher(str(g_informatika), 0))

    reg_users(message)