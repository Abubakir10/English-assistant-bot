import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from handlers import bot_handler
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher()


logger = logging.getLogger(__name__)


async def register_handlers(dp: Dispatcher):
    dp.message.register(bot_handler.start, Command('start'))
    dp.message.register(bot_handler.menu, Command('main_menu'))
    dp.message.register(bot_handler.schedule, Command('schedule'))
    dp.message.register(bot_handler.fee, Command('fee'))
    dp.message.register(bot_handler.basic_fee, Command('basic'))
    dp.message.register(bot_handler.standart_fee, Command('standart'))
    dp.message.register(bot_handler.premium_fee, Command('premium'))
    dp.message.register(bot_handler.payg_fee, Command('pay_as_you_go'))
    dp.message.register(bot_handler.promotion, Command('promotions'))


    # callbacks
    dp.callback_query.register(bot_handler.start_callback, F.data == 'start')
    dp.callback_query.register(bot_handler.menu_callback, F.data == 'main_menu')
    dp.callback_query.register(bot_handler.schedule_callback, F.data == 'schedule')
    dp.callback_query.register(bot_handler.fee_callback, F.data == 'fee')
    dp.callback_query.register(bot_handler.basic_fee_callback, F.data == 'basic')
    dp.callback_query.register(bot_handler.standart_fee_callback, F.data == 'standart')
    dp.callback_query.register(bot_handler.premium_fee_callback, F.data == 'premium')
    dp.callback_query.register(bot_handler.payg_fee_callback, F.data == 'pay_as_you_go')
    dp.callback_query.register(bot_handler.promotion_callback, F.data == 'promotions')



async def main():
    # Регистрация обработчиков
    await register_handlers(dp)

    logger.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
