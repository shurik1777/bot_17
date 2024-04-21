import asyncio
import logging
from os import getenv
from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from app_wedding.db.models import async_main
from app_wedding.handlers import router

load_dotenv(find_dotenv())


async def main():
    await async_main()
    bot = Bot(token=getenv('TOKEN'),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
