from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

grade = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='one')],
    [InlineKeyboardButton(text='2', callback_data='two')],
    [InlineKeyboardButton(text='3', callback_data='three')],
    [InlineKeyboardButton(text='4', callback_data='four')],
    [InlineKeyboardButton(text='5', callback_data='five')],
    [InlineKeyboardButton(text='6', callback_data='six')],
    [InlineKeyboardButton(text='7', callback_data='seven')],
    [InlineKeyboardButton(text='8', callback_data='eight')],
    [InlineKeyboardButton(text='9', callback_data='nine')],
    [InlineKeyboardButton(text='10', callback_data='ten')]
])

guest = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да', callback_data='yes')],
    [InlineKeyboardButton(text='Нет', callback_data='no')],
    [InlineKeyboardButton(text='Возможно', callback_data='maybe')]
])

theme = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Очень понравилось!', callback_data='very')],
    [InlineKeyboardButton(text='Что-то среднее...', callback_data='fifty')],
    [InlineKeyboardButton(text='Не очень...', callback_data='notvery')]
])

next_theme = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='next_theme')]
])

next_review = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее', callback_data='next_review')]
])