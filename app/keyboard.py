from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [[KeyboardButton(text="список работ"),
      KeyboardButton(text="магазин запчастей"),
      KeyboardButton(text="мастера")]]

setting_kb = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True)
    # input_field_placeholder="Нажмите кнопку для вывода информации")