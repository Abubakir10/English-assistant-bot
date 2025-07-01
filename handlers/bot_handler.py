from mailbox import Message

from aiogram import types
from handlers import texts, keyboards
from aiogram.types import FSInputFile


async def start(message: types.Message):
    photo = types.FSInputFile("images/english_book.jpg")
    await message.answer_photo(
        photo=photo,
        caption=texts.start_tx,
        reply_markup=keyboards.start_kb(),
        parse_mode='HTML'
    )

async def start_callback(callback: types.CallbackQuery):
    photo = types.FSInputFile("images/english_book.jpg")
    await callback.message.answer_photo(
        photo=photo,
        caption=texts.start_tx,
        reply_markup=keyboards.start_kb(),
        parse_mode='HTML'
    )
    await callback.answer()



async def menu(message: types.Message):
    my_phono = types.FSInputFile("images/eltam.png")
    await message.answer_photo(
            photo=my_phono,
            caption=texts.menu_tx,
            reply_markup=keyboards.get_schedule(),
            parse_mode='HTML'
        )

async def menu_callback(callback: types.CallbackQuery):
    my_phono = types.FSInputFile("images/eltam.png")
    await callback.message.answer_photo(
            photo=my_phono,
            caption=texts.menu_tx,
            reply_markup=keyboards.get_schedule(),
            parse_mode='HTML'
        )
    await callback.answer()


async def schedule(message: types.Message):
    photo = types.FSInputFile("images/schedule.png")
    await message.answer_photo(
        photo=photo,
        caption=texts.schedule_tx,
        reply_markup=keyboards.get_schedule(),
        parse_mode='HTML'
    )

async def schedule_callback(callback: types.CallbackQuery):
    photo = types.FSInputFile("images/schedule.png")
    await callback.message.answer_photo(
        photo=photo,
        caption=texts.schedule_tx,
        reply_markup=keyboards.get_schedule(),
        parse_mode='HTML'
    )
    await callback.answer()


async def fee(message: types.Message):
    photo = types.FSInputFile("images/fee.png")
    await message.answer_photo(
        photo=photo,
        caption=texts.fee_tx,
        reply_markup=keyboards.get_fee(),
        parse_mode='HTML'
    )

async def fee_callback(callback: types.CallbackQuery):
    photo = types.FSInputFile("images/fee.png")
    await callback.message.answer_photo(
        photo=photo,
        caption=texts.fee_tx,
        reply_markup=keyboards.get_fee(),
        parse_mode='HTML'
    )
    await callback.answer()



async def basic_fee(message: types.Message):
    await message.answer_photo(
        photo= types.FSInputFile('images/basic_fee_photo.jpeg'),
        caption=texts.basic_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )

async def basic_fee_callback(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo= types.FSInputFile('images/basic_fee_photo.jpeg'),
        caption=texts.basic_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )
    await callback.answer()



async def standart_fee(message: types.Message):
    await message.answer_photo(
        photo= types.FSInputFile('images/standart_fee_photo.jpeg'),
        caption=texts.standart_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )

async def standart_fee_callback(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo= types.FSInputFile('images/standart_fee_photo.jpeg'),
        caption=texts.standart_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )
    await callback.answer()



async def premium_fee(message: types.Message):
    await message.answer_photo(
        photo= types.FSInputFile('images/premium_fee_photo.jpeg'),
        caption=texts.premium_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )

async def premium_fee_callback(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo= types.FSInputFile('images/premium_fee_photo.jpeg'),
        caption=texts.premium_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )
    await callback.answer()


async def payg_fee(message: types.Message):
    await message.answer_photo(
        photo= types.FSInputFile('images/payg_fee_photo.png '),
        caption=texts.pay_as_you_go_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )

async def payg_fee_callback(callback: types.CallbackQuery):
    await callback.message.answer_photo(
        photo= types.FSInputFile('images/payg_fee_photo.png'),
        caption=texts.pay_as_you_go_fee_tx,
        reply_markup=keyboards.get_promotion(),
        parse_mode='HTML'
    )
    await callback.answer()

async def promotion(message: types.Message):
    photo = types.FSInputFile('images/promotion.jpg')
    await message.answer_photo(
        photo=photo,
        caption=texts.promotions_tx,
        reply_markup=keyboards.get_fee(),
        parse_mode='HTML'
    )

async def promotion_callback(callback: types.CallbackQuery):
    photo = types.FSInputFile('images/promotion.jpg')
    await callback.message.answer_photo(
        photo=photo,
        caption=texts.promotions_tx,
        reply_markup=keyboards.get_fee(),
        parse_mode='HTML'
    )
    await callback.answer()