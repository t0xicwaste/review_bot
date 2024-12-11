from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Регистрация', callback_data='register')],
    [InlineKeyboardButton(text='Написать отзыв', callback_data='review')],
])