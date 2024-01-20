from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.database.models import OktanBD
from app.keyboard import main_keyboard, mkb_main_keyboard, menu_master
from app.messages import WELCOME, DESCRIPTION

okb = OktanBD()
router_kb = Router()

############### Обычные кнопки при старте ###############


@router_kb.message(CommandStart())
async def cmd_start(message: Message):
    main_keyboard.kb
    await message.answer(f"Привет {message.from_user.full_name}. {WELCOME}",
                         reply_markup=main_keyboard.setting_kb)
    await message.delete()


@router_kb.message(F.text.upper() == 'ВОЙТИ')
async def welcom(message: Message):
    await message.answer(DESCRIPTION,\
                         reply_markup=mkb_main_keyboard.setting_mkb)
    await message.delete()


############### "Записаться" подкнопки выбор ###############
    
@router_kb.message(F.text.upper() == "ЗАПИСАТЬСЯ")
async def sign_up(message: Message):
    name = message.from_user.first_name
    username = message.from_user.username
    okb.main(name=name, username=username)
    await message.answer(text=f"{name} вам перезвонят")
    await message.delete()


@router_kb.message(F.text.lower() == "назад")
async def back_welcome(message: Message):
    await message.answer(WELCOME,
                         reply_markup=main_keyboard.setting_kb)
    await message.delete()


@router_kb.message(F.text.lower() == "назад")
async def back_description(message: Message):
    await message.answer(DESCRIPTION,
                         reply_markup=menu_master.setting_mmkb)


############### Отлавливает все ненужные сообщения ###############

@router_kb.message()
async def trash_msg(message: Message):
    await message.answer(WELCOME,
                         reply_markup=main_keyboard.setting_kb)