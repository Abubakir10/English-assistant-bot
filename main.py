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
    dp.message.register(bot_handler.menu, Command('menu'))

    # callbacks
    dp.callback_query.register(bot_handler.menu, F.data == 'menu')


async def main():
    # Регистрация обработчиков
    await register_handlers(dp)

    logger.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
