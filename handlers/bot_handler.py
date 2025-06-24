from aiogram import types
from handlers import texts, keyboards
from aiogram.types import FSInputFile


async def start(message: types.Message = None, callback: types.CallbackQuery = None):
    photo = types.FSInputFile("images/python-book.jpg")
    # Обработка команды /start
    await callback.answer_photo(
            photo=photo,
            caption=texts.start_tx,
            reply_markup=keyboards.start_kb(),
            parse_mode='HTML'
        )
    await callback.answer()



async def menu(callback: types.CallbackQuery):
    my_phono = ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwU2iR2zza-LievOJTBSckwORkXzG2qiPBVQ&s")
    await callback.answer_photo(
            photo=my_phono,
            caption=texts.menu_tx,
            reply_markup=keyboards.get_schedule(),
            parse_mode='HTML'
        )
    await callback.answer()



