from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,\
                              InlineKeyboardButton, InlineKeyboardMarkup

from app.messages import TECHNICAL_SERVICE, TIRE_FITTING,\
                        THE_COLLAPSE_OF_CONVERGENCE, COMPLEX_REPAIRS

############### Обычные кнопки при старте ###############

class MainKeyboard:
      kb = [[KeyboardButton(text="список работ"),
            KeyboardButton(text="магазин запчастей"),
            KeyboardButton(text="мастера")]]
      setting_kb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                          input_field_placeholder="СТО Окта")

############### Инлайн подкнопки выбор ###############

class InlineMainKeyboard:
      ikb = [[InlineKeyboardButton(text=TIRE_FITTING,\
                                   callback_data="tire_fitting")],
             [InlineKeyboardButton(text=THE_COLLAPSE_OF_CONVERGENCE,\
                                   callback_data="the_collapse_of_convergence")],
             [InlineKeyboardButton(text=TECHNICAL_SERVICE,\
                                   callback_data='technical_service')],
             [InlineKeyboardButton(text=COMPLEX_REPAIRS,\
                                   callback_data="complex_repairs")]]
            #  [InlineKeyboardButton(text="назад")]]
      setting_ikb = InlineKeyboardMarkup(inline_keyboard=ikb)


############## Запуск клавиатур ##############

main_keyboard = MainKeyboard()
ikb_main_keyboard = InlineMainKeyboard()
      