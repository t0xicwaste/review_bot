from aiogram import F, Router
from aiogram.types import CallbackQuery, Message

from aiogram.fsm.context import FSMContext
from FSM.state_review import Reviews

from database.connection import session_factory
from database.model_review import Review

from keyboards import review_kb as kb

from dict.dict_review import GRADE, GUEST, THEME, NEXT_THEME, NEXT_REVIEW

rev_router = Router()

@rev_router.callback_query(F.data == 'review')
async def start_review(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='И вновь привет! Пожалуйста, оставьте свой отзыв с впечатлениями от встречи: ')
    await callback.message.answer(text='Оцените от 1 до 10 прошедшую встречу', reply_markup=kb.grade)
    await state.set_state(Reviews.grade)

@rev_router.callback_query(F.data.in_(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']), Reviews.grade)
async def input_guest(callback: CallbackQuery, state: FSMContext):
    await state.update_data(grade=callback.data)
    await callback.message.answer(text='Готовы ли вы пригласить друзей в наш дискуссионный клуб на следующие встречи?', reply_markup=kb.guest)
    await state.set_state(Reviews.guest)

@rev_router.callback_query(F.data.in_(['yes', 'no', 'maybe']), Reviews.guest)
async def input_theme(callback: CallbackQuery, state: FSMContext):
    await state.update_data(guest=callback.data)
    await callback.message.answer(text='Понравилась ли вам тема нашей встречи?', reply_markup=kb.theme)
    await state.set_state(Reviews.theme)

@rev_router.callback_query(F.data.in_(['very', 'fifty', 'notvery']), Reviews.theme)
async def input_next_theme(callback: CallbackQuery, state: FSMContext):
    await state.update_data(theme=callback.data)
    await callback.message.answer(text='Какую бы тему вы хотели видеть в следующий раз?', reply_markup=kb.next_theme)
    await state.set_state(Reviews.next_theme)

# Функция обработки ввода сообщений и нажатия на кнопку далее для оценки темы

@rev_router.callback_query(F.data.in_(['next_theme']), Reviews.next_theme)
async def input_next_review_and_final_theme(event: CallbackQuery | Message, state: FSMContext):
    if isinstance(event, CallbackQuery):
        await state.update_data(next_theme=event.data)
    elif isinstance(event, Message):
        await state.update_data(next_theme=event.text)
    await (event.message if isinstance(event, CallbackQuery) else event).answer(text='Здесь вы можете написать все свои предложения/желания/критику', reply_markup=kb.next_review)
    await state.set_state(Reviews.next_review)

# Функция обработки ввода сообщений и нажатия на кнопку далее для отзыва

@rev_router.callback_query(F.data.in_(['next_review']), Reviews.next_review)
async def input_next_review(event: CallbackQuery | Message, state: FSMContext):
    if isinstance(event, CallbackQuery):
        await state.update_data(next_review=event.data)
    elif isinstance(event, Message):
        await state.update_data(next_review=event.text)
    user_data = await state.get_data()

    formatted_review = f"""
Спасибо за отзыв!
"""

    # Отправка итогового сообщения
    await (event.message if isinstance(event, CallbackQuery) else event).answer(text=formatted_review)
    await state.clear()

    async with session_factory() as session:
        new_review = Review(
            first_name=event.from_user.first_name,
            grade=user_data['grade'],
            guest=user_data['guest'],
            theme=user_data['theme'],
            next_theme=user_data['next_theme'],
            next_review=user_data['next_review']
        )
        session.add(new_review)
        await session.commit()