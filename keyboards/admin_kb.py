from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки клавиатуры админа
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('/Меню')).add(
    KeyboardButton('/Загрузить')).add(
    KeyboardButton('/Удалить'))

# кнопки сслыки
urlkb = InlineKeyboardMarkup(row_width=2)
inline_buttons_list = [
    InlineKeyboardButton(text='40R', url='https://40r.ru'),
    InlineKeyboardButton(text='24ON', url='https://24on.ru'),
]
urlkb.add(*inline_buttons_list)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми меня', callback_data='www'))
