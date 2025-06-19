from aiogram import types
from handlers import texts, keyboards

async def start(message: types.Message):
    await message.answer(
        text=texts.start_tx,
        reply_markup=keyboards.start_kb(),
        parse_mode='HTML'
    )




