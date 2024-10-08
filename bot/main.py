import asyncio
import logging
import sys

from aiogram import Dispatcher

from core.logger import logger
from core.bot import main_bot
from start import router as start_router


async def main():
    dp = Dispatcher()
    dp.include_routers(
        start_router,
    )
    logger.debug("Start")
    await dp.start_polling(main_bot)
    logger.debug("Stop")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
