from aiogram import types, F, Bot, Dispatcher
from aiogram.utils.keyboard import InlineKeyboardBuilder
import logging
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

from handlers import texts
from handlers import keyboards



async def start(message: types.Message = None, callback: types.CallbackQuery = None):
    if isinstance(message, types.Message):
        await callback.answer(
            text=texts.start_tx,
            reply_markup=keyboards.start_kb(),
            parse_mode = 'HTML'
        )

    return callback.answer()



