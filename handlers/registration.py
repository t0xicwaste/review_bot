from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.context import FSMContext
from FSM.state_reg import Registrations

from database.connection import session_factory
from database.model_registration import Registration

reg_router = Router()

@reg_router.callback_query(F.data == "register")
async def register_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Привет! Для ого чтобы попасть на дискуссионный клуб, вам нужно пройти регистрацию.')
    await state.set_state(Registrations.name)
    await callback.message.answer(text='Введите ваше имя:')

@reg_router.message(Registrations.name)
async def drink(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registrations.drink)
    await message.answer(text='Какой напиток вы предпочитаете?\n(чай, кофе, сок или другой напиток)')

@reg_router.message(Registrations.drink)
async def eat(message: Message, state: FSMContext):
    await state.update_data(drink=message.text)
    await message.answer(text='Какую еду вы предпочитаете: ')
    await state.set_state(Registrations.eat)

@reg_router.message(Registrations.eat)
async def final_state(message: Message, state: FSMContext):
    await state.update_data(eat=message.text)
    data = await state.get_data()
    await message.answer(text='Ваша регистрация завершена!')
    await state.clear()

    async with session_factory() as session:
        new_registration = Registration(
                tg_id=message.from_user.id,
                first_name=data['name'],
                drink=data['drink'],
                eat=data['eat']
            )
        session.add(new_registration)
        await session.commit()