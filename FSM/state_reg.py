from aiogram.fsm.state import State, StatesGroup

class Registrations(StatesGroup):
    name = State()
    drink = State()
    eat = State()
    tg_id = State()