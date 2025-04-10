import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
import asyncio

from core.config import BOT_TOKEN
from handlers import user_handler
from utils.double_logging import DoubleWrite


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрация обработчиков
    dp.include_router(user_handler.router)

    # Логгирование в консоль и файл
    logfile = open("py_log.log", "r+")
    logfile.seek(0, 2)
    logging.basicConfig(level=logging.INFO, stream=DoubleWrite(sys.stdout, logfile))

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
