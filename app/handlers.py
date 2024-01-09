from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.keyboard import kb, setting_kb
from app.messages import ACTION_USER


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    kb
    await message.answer(f"Привет {message.from_user.full_name}\n{ACTION_USER}",
                         reply_markup=setting_kb)


@router.message(F.text.lower() == "список работ")
async def list_of_work(message: Message):
    await message.answer("Различные работы")


@router.message(F.text.lower() == "магазин запчастей")
async def list_of_work(message: Message):
    await message.answer("Различные запчасти")

    
@router.message(F.text.lower() == "мастера")
async def list_of_work(message: Message):
    await message.answer("Различные мастера")