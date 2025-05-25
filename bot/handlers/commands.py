from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.messages import (
    START_MESSAGE,
    QA_MESSAGE,
    COURSES_MESSAGE,
    HELP_MESSAGE,
)


async def h_start(message: Message, state: FSMContext):
    await message.answer(
        text=START_MESSAGE,
        parse_mode=ParseMode.HTML,
    )
    await state.clear()


async def h_qa(message: Message, state: FSMContext):
    await message.answer(
        text=QA_MESSAGE,
        parse_mode=ParseMode.HTML,
    )
    await state.clear()


async def h_courses(message: Message, state: FSMContext):
    await message.answer(
        text=COURSES_MESSAGE,
        parse_mode=ParseMode.HTML,
    )
    await state.clear()


async def h_help(message: Message, state: FSMContext):
    await message.answer(
        text=HELP_MESSAGE,
        parse_mode=ParseMode.HTML,
    )
    await state.clear()
