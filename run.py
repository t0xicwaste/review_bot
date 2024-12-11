import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from database.connection import flush_db, engine

from handlers.start import router
from handlers.review import rev_router
from handlers.registration import reg_router

from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def db_startup(dispatcher: Dispatcher):
    await flush_db(engine=engine)

async def main():
    dp.include_router(router)
    dp.include_router(rev_router)
    dp.include_router(reg_router)
    await db_startup(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
