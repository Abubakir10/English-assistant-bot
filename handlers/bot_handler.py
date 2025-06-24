from aiogram import types
from handlers import texts, keyboards
from aiogram.types import FSInputFile


async def start(message: types.Message):
    my_phono = FSInputFile("images/python-book.jpg")
    await message.answer_photo(
        photo=my_phono,
        caption=texts.start_tx,
        reply_markup=keyboards.start_kb(),
        parse_mode="HTML"
    )





