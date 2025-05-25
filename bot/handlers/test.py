from collections import defaultdict

from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.test import questions
from bot.utils.fsm import StateMachine
from bot.utils.messages import RESULT_DESIGN_MESSAGE, RESULT_BUISINESS_MESSAGE, TEST_START_MESSAGE, RESULT_MESSAGE


async def h_start_test(message: Message, state: FSMContext):
    await message.answer(
        text=TEST_START_MESSAGE,
        parse_mode=ParseMode.HTML,
    )

    await state.update_data(
        questions=questions,
        current_question=0,
        score=defaultdict(int),
    )

    state_data = await state.get_data()
    current_question = state_data.get('current_question')
    question = state_data.get('questions')[current_question]

    await message.answer(
        text=question.to_text(current_question + 1),
        parse_mode=ParseMode.HTML,
    )

    await state.set_state(StateMachine.test)


async def h_answer_test(message: Message, state: FSMContext):
    try:
        number = int(message.text) - 1
    except ValueError:
        await message.answer(
            text='Пожалуйста, введите номер ответа.',
            parse_mode=ParseMode.HTML,
        )
        return

    state_data = await state.get_data()
    current_question = state_data.get('current_question')
    questions = state_data.get('questions')
    question = questions[current_question]
    score = state_data.get('score')

    try:
        current_score = question.get_score(number)
    except ValueError as e:
        await message.answer(
            text=str(e),
            parse_mode=ParseMode.HTML,
        )
        return

    score[current_score] += 1
    await state.update_data(score=score)

    current_question += 1
    if current_question >= len(questions):
        if score[2] > score[1]:
            msg = RESULT_DESIGN_MESSAGE
        else:
            msg = RESULT_BUISINESS_MESSAGE
        await message.answer(
            text=RESULT_MESSAGE.format(msg),
            parse_mode=ParseMode.HTML,
        )
        await state.clear()
        return
    
    await state.update_data(current_question=current_question)
    question = questions[current_question]

    await message.answer(
        text=question.to_text(current_question + 1),
        parse_mode=ParseMode.HTML,
    )
