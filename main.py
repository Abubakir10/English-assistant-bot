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

async def on_startup():
    """Функция, выполняемая при запуске бота"""
    logger.info("Бот успешно запущен")

async def on_shutdown():
    """Функция, выполняемая при выключении бота"""
    logger.info("Бот выключается...")


async def register_handlers(dp: Dispatcher):
    dp.message.register(bot_handler.start, Command('start'))


async def main():
    # Регистрация обработчиков
    await register_handlers(dp)

    # Установка функций запуска/остановки
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    logger.info("Запуск бота...")
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
