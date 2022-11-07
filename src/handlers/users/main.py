from aiogram import types

from aiogram.dispatcher.filters import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def doStart(message: types.Message):
    TEXT = "Assalomu alaykum"
    await message.answer(TEXT)
