from aiogram import Router, types
from aiogram.filters.command import Command, CommandStart


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")