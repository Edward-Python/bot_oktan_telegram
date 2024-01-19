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





# @router_kb.message(F.text.upper() == 'ВОЙТИ')
# async def photo_welcom(message: Message):    
#     photo = "bot_oktan/app/configs/sto_oktan.png"
#     await message.answer_photo(photo=FSInputFile(photo))



# @router_kb.message(F.text.upper() == "МАГАЗИН ЗАПЧАСТЕЙ")
# async def spare_parts_store(message: Message):
#     await message.answer("В разработке !")

    
# @router_kb.message(F.text.upper() == "МАСТЕРА")
# async def masters(message: Message):
#     await message.answer(MASTERS,\
#                          reply_markup=menu_master.setting_mmkb)


############### "Список работ" подкнопки выбор ###############
    
    ############# кнопки "Шиномонтаж" ##############
@router_kb.message(F.text.upper() == "ЗАПИСАТЬСЯ")
async def sign_up(message: Message):
    name = message.from_user.first_name
    username = message.from_user.username
    okb.main(name=name, username=username)
    await message.answer(text=f"{name} вам перезвонят")


# @router_kb.callback_query(F.data == "sign up")
# async def ikb_list_of_work_tire_fitting_r13(callback: CallbackQuery):
#     name = callback.from_user.first_name
#     username = callback.from_user.username
#     okb.main(name=name, username=username)
#     await callback.message.edit_text(text=f"{callback.from_user.first_name} вам перезвонят")






# @router_kb.message(F.text.upper() == THE_COLLAPSE_OF_CONVERGENCE)
# async def mkb_list_of_work_the_collapse_of_convergence(message: Message):
#     await message.answer(DESCRIPTION_DESCRIPTION_TIRE_FITTING)


# @router_kb.message(F.text.upper() == TECHNICAL_SERVICE)
# async def mkb_list_of_work_technical_service(message: Message):
#     await message.answer(DESCRIPTION_TECHNICAL_SERVICE)


# @router_kb.message(F.text.upper() == COMPLEX_REPAIRS)
# async def mkb_list_of_work_complex_repairs(message: Message):
#     await message.answer(DESCRIPTION_COMPLEX_REPAIRS)


@router_kb.message(F.text.lower() == "назад")
async def back_welcome(message: Message):
    await message.answer(WELCOME,
                         reply_markup=main_keyboard.setting_kb)
    

############### "Список работ" подкнопки выбор ###############

@router_kb.message(F.text.lower() == "назад")
async def back_description(message: Message):
    await message.answer(DESCRIPTION,
                         reply_markup=menu_master.setting_mmkb)


############### Отлавливает все ненужные сообщения ###############

@router_kb.message()
async def trash_msg(message: Message):
    await message.answer(WELCOME,
                         reply_markup=main_keyboard.setting_kb)