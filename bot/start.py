from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from services.currencies import get_exchange_rate

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer("Добрый день. Как вас зовут?")


@router.message()
async def command_name(message: Message, state: FSMContext) -> None:
    if message.text:
        user_last_name = message.text

        exchange_rate = await get_exchange_rate("USD")
        if not exchange_rate:
            await message.answer(
                f"Рад знакомству, {user_last_name}! К сожалению, возникла ошибка. Пожалуйста, попробуйте обратиться позже."
            )
        else:
            await message.answer(
                f"Рад знакомству, {user_last_name}! Курс доллара сегодня согласно данными ЦБ РФ: {exchange_rate} рубля."
            )
    else:
        await message.answer(
            "Пожалуйста, укажите ваше имя в текстовом виде, чтобы мы могли познакомиться!"
        )
