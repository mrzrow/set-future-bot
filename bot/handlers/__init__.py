__all__ = (
    'create_commands',
    'register_commands'
)

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import BotCommand

from bot.utils.fsm import StateMachine
from .test import h_start_test, h_answer_test
from .commands import (
    h_start,
    h_qa,
    h_courses,
    h_help,
)


def create_commands():
    bot_commands = [
        ('start', 'Начать диалог с ботом'),
        ('qa', 'Часто задаваемые вопросы'),
        ('courses', 'Информация о курсах'),
        ('help', 'Задать вопрос'),
        ('test', 'Пройти тест'),
    ]
    return [BotCommand(command=cmd[0], description=cmd[1]) for cmd in bot_commands]


def register_commands(router: Router):
    router.message.register(h_start, Command(commands=['start']))
    router.message.register(h_qa, Command(commands=['qa']))
    router.message.register(h_courses, Command(commands=['courses']))
    router.message.register(h_help, Command(commands=['help']))
    
    router.message.register(h_start_test, Command(commands=['test']))
    router.message.register(h_answer_test, StateMachine.test)
