from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from app.keyboard import main_keyboard, ikb_main_keyboard
from app.messages import ACTION_USER, DESCRIPTION_TECHNICAL_SERVICE,\
                        DESCRIPTION_DESCRIPTION_TIRE_FITTING,\
                        DESCRIPTION_TIRE_FITTING, DESCRIPTION_COMPLEX_REPAIRS


router_kb = Router()

############### Обычные кнопки при старте ###############


@router_kb.message(CommandStart())
async def cmd_start(message: Message):
    main_keyboard.kb
    await message.answer(f"Привет {message.from_user.full_name}. {ACTION_USER}",
                         reply_markup=main_keyboard.setting_kb)


@router_kb.message(F.text.lower() == "список работ")
async def list_of_work(message: Message):
    await message.answer("Различные работы",\
                         reply_markup=ikb_main_keyboard.setting_ikb)


@router_kb.message(F.text.lower() == "магазин запчастей")
async def spare_parts_store(message: Message):
    await message.answer("Различные запчасти")

    
@router_kb.message(F.text.lower() == "мастера")
async def masters(message: Message):
    await message.answer("Различные мастера")


@router_kb.message()
async def trash_msg(message: Message):
    await message.answer(f"{message.from_user.full_name}. {ACTION_USER}",
                         reply_markup=main_keyboard.setting_kb)


############### Инлайн "Список работ" подкнопки выбор ###############

@router_kb.callback_query(F.data == "tire_fitting")
async def ikb_list_of_work_tire_fitting(callback: CallbackQuery):
    await callback.message.edit_text(text=DESCRIPTION_TIRE_FITTING,\
                reply_markup=callback.message.reply_markup)
    
@router_kb.callback_query(F.data == "the_collapse_of_convergence")
async def ikb_list_of_work_the_collapse_of_convergence(callback: CallbackQuery):
    await callback.message.edit_text(text=DESCRIPTION_DESCRIPTION_TIRE_FITTING,\
                reply_markup=callback.message.reply_markup)
    
@router_kb.callback_query(F.data == "technical_service")
async def ikb_list_of_work_technical_service(callback: CallbackQuery):
    await callback.message.edit_text(text=DESCRIPTION_TECHNICAL_SERVICE,\
                reply_markup=callback.message.reply_markup)
    
@router_kb.callback_query(F.data == "complex_repairs")
async def ikb_list_of_work_complex_repairs(callback: CallbackQuery):
    await callback.message.edit_text(text=DESCRIPTION_COMPLEX_REPAIRS,\
                reply_markup=callback.message.reply_markup)