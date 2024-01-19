from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,\
                              InlineKeyboardButton, InlineKeyboardMarkup

from app.messages import TECHNICAL_SERVICE, TIRE_FITTING,\
                        THE_COLLAPSE_OF_CONVERGENCE, COMPLEX_REPAIRS

############### Обычные кнопки при старте ###############

class MainKeyboard:
      kb = [[KeyboardButton(text='ВОЙТИ')]]
            #  KeyboardButton(text="МАГАЗИН ЗАПЧАСТЕЙ"),
            #  KeyboardButton(text="МАСТЕРА")]]
      setting_kb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                          input_field_placeholder="СТО Октан")
      

class MenuMainKeyboard:
      mkb = [[KeyboardButton(text="ЗАПИСАТЬСЯ")],\
            #   KeyboardButton(text=THE_COLLAPSE_OF_CONVERGENCE)],
            #  [KeyboardButton(text=TECHNICAL_SERVICE),\
            #   KeyboardButton(text=COMPLEX_REPAIRS)],
             [KeyboardButton(text="назад")]]
      setting_mkb = ReplyKeyboardMarkup(keyboard=mkb, resize_keyboard=True,
                                          input_field_placeholder="СТО Окта")
      

class MenuMaster:
      mmkb = [[KeyboardButton(text="назад")]]
      setting_mmkb = ReplyKeyboardMarkup(keyboard=mmkb, resize_keyboard=True,
                                          input_field_placeholder="СТО Окта")


############### Инлайн подкнопки Шиномонтаж ###############

class InlineKeyboardSignUp:
      ikbsu = [[InlineKeyboardButton(text="Записаться",\
                                   callback_data="sign up")]]
      setting_ikbsu = InlineKeyboardMarkup(inline_keyboard=ikbsu)


############## Запуск клавиатур ##############

main_keyboard = MainKeyboard()
# ikb_main_keyboard = InlineMainKeyboard()
mkb_main_keyboard = MenuMainKeyboard()
menu_master = MenuMaster()
inline_keyboard_sign_up = InlineKeyboardSignUp()
      