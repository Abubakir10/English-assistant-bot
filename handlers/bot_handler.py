from aiogram import types
from handlers import texts, keyboards
from aiogram.types import FSInputFile


async def start(message: types.Message):
    photo = types.FSInputFile("images/python-book.jpg")
    await message.answer_photo(
        photo=photo,
        caption=texts.start_tx,
        reply_markup=keyboards.start_kb(),
        parse_mode='HTML'
    )

async def start_callback(callback: types.CallbackQuery):
    photo = types.FSInputFile("images/python-book.jpg")
    await callback.message.answer_photo(
        photo=photo,
        caption=texts.start_tx,
        reply_markup=keyboards.start_kb(),
        parse_mode='HTML'
    )
    await callback.answer()



async def menu(message: types.Message):
    my_phono = ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwU2iR2zza-LievOJTBSckwORkXzG2qiPBVQ&s")
    await message.answer_photo(
            photo=my_phono,
            caption=texts.menu_tx,
            reply_markup=keyboards.get_schedule(),
            parse_mode='HTML'
        )

async def menu_callback(callback: types.CallbackQuery):
    my_phono = ("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwU2iR2zza-LievOJTBSckwORkXzG2qiPBVQ&s")
    await callback.message.answer_photo(
            photo=my_phono,
            caption=texts.menu_tx,
            reply_markup=keyboards.get_schedule(),
            parse_mode='HTML'
        )
    await callback.answer()


async def schedule(message: types.Message):
    photo = ("https://www.bigtime.net/wp-content/uploads/2024/02/Schedule-Conflicts_-How-to-Deal-with-Them-and-Benefit-From-the-Challenge.png")
    await message.answer_photo(
        photo=photo,
        caption=texts.schedule_tx,
        reply_markup=keyboards.get_schedule(),
        parse_mode='HTML'
    )

async def schedule_callback(callback: types.CallbackQuery):
    photo = ("https://www.bigtime.net/wp-content/uploads/2024/02/Schedule-Conflicts_-How-to-Deal-with-Them-and-Benefit-From-the-Challenge.png")
    await callback.message.answer_photo(
        photo=photo,
        caption=texts.schedule_tx,
        reply_markup=keyboards.get_schedule(),
        parse_mode='HTML'
    )
    await callback.answer()
