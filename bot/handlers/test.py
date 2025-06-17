from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.test import questions, Quiz
from bot.utils.fsm import StateMachine
from bot.utils.messages import TEST_START_MESSAGE


async def h_start_test(message: Message, state: FSMContext):
    await message.answer(
        text=TEST_START_MESSAGE,
        parse_mode=ParseMode.HTML,
    )

    quiz = Quiz(questions=questions)

    await message.answer(
        text=quiz.get_question_text(),
        parse_mode=ParseMode.HTML
    )

    await state.set_state(StateMachine.test)
    await state.update_data(quiz=quiz)


async def h_answer_test(message: Message, state: FSMContext):
    if not message.text.isdigit():  # проверяем, что пришло число
        return await message.answer(
            text='Введите, пожалуйста, корректный номер ответа',
            parse_mode=ParseMode.HTML
        )
    
    data = await state.get_data()
    quiz: Quiz = data.get('quiz')
    answer_number = int(message.text) - 1
    try:  # проверяем число на корректность и учитываем результат
        quiz.set_result(answer_number=answer_number)
    except ValueError as e:
        return await message.answer(
            text=f'{e}',
            parse_mode=ParseMode.HTML
        )
    
    quiz.move_to_next_question()  # переходим к следующему вопросу
    if quiz.is_end():  # если вопросы закончились, то выводим результат
        await message.answer(
            text=quiz.get_result_message(),
            parse_mode=ParseMode.HTML
        )
        return await state.clear()
    
    await message.answer(  # выводим текст следующего вопроса
        quiz.get_question_text(),
        parse_mode=ParseMode.HTML
    )
    await state.update_data(quiz=quiz)
