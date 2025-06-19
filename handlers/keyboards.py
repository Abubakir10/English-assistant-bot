from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


# Универсальный генератор клавиатуры
def create_kb(buttons: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for text, cb in buttons:
        kb.button(text=text, callback_data=cb)
    kb.adjust(1)
    return kb.as_markup()


# Главное меню
def start_kb():
    return create_kb([('🚀Начать', 'main_menu')])


