from aiogram import types

from loader import dp
from keyboards.keyboard import *
from utils.phrazes import *
from utils.func import *


@dp.message_handler(commands=back)
async def back(message: types.Message):
    if str(message.from_user.id) in block_user["blocked"]:
        await message.answer("Извините, вы находитесь в черном списке. Если вы считаете что попали туда ошибочно, напишите создателю: @darkusha_ds")
        return
    await message.answer('Вы вернулись в главное меню', reply_markup=welcome_key)