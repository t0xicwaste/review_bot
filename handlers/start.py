from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import review_kb as kb
from keyboards import start_kb as kb

router = Router()

# functions grades
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_sticker("CAACAgIAAxkBAAENFNJnK-R3_V77DEVPnQQF46CglHasSgACvUAAAuVzYEqLNc48PMgD8TYE")
    await message.answer("Привет, выбери действие!", reply_markup=kb.start)
