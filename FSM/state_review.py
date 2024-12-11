from aiogram.fsm.state import State, StatesGroup

class Reviews(StatesGroup):
    grade = State()
    guest = State()
    theme = State()
    next_theme = State()
    next_review = State()