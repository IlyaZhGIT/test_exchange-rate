from aiogram import Bot

from core.config import env


class MyBot:
    TOKEN = env.BOT_TOKEN
    main_bot: Bot = Bot(token=TOKEN)


main_bot = MyBot.main_bot
