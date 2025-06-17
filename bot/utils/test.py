from collections import Counter

from .study_enum import Study
from .messages import RESULT_MESSAGE, COURSES_BULLET_POINTS, COURSES_NAMES


class Question:
    def __init__(
            self,
            question: str,
            answers: tuple[str, ...],
            points: tuple[tuple[Study, Study], ...]
    ):
        self.question = question
        self.answers = answers
        self.points = points
        self.questions_number = len(self.answers)
    
    def get_answer(self, answer_number: int) -> tuple[Study, Study]:
        if answer_number < 0 or answer_number >= self.questions_number:
            raise ValueError('Неверный номер ответа')
        return self.points[answer_number]

    def get_question_text(self) -> str:
        msg = f'{self.question}\n'
        for i, answ in enumerate(self.answers, 1):
            msg += f'{i}. {answ}\n'
        return msg


class Quiz:
    def __init__(self, questions: tuple[Question, ...]):
        self.questions = questions
        self.iter = 0
        self.counter = Counter()

    def move_to_next_question(self) -> None:
        self.iter += 1

    def is_end(self) -> bool:
        return self.iter >= len(questions)
    
    def get_question_text(self) -> str:
        return self.questions[self.iter].get_question_text()
    
    def set_result(self, answer_number: int) -> None:
        result = self.questions[self.iter].get_answer(answer_number=answer_number)
        self.counter.update(result)

    def get_result_message(self) -> str:
        course = self.counter.most_common(1)[0][0]
        msg = RESULT_MESSAGE.format(COURSES_BULLET_POINTS[course], COURSES_NAMES[course])
        return msg
    

questions = (
    Question(
        question='<b>Что тебе интереснее всего?</b> 🧡',
        answers=(
            'Разобраться, как устроена компания изнутри',
            'Создавать визуальную часть проекта (дизайн, верстка)',
            'Делать креативный контент, снимать, писать',
            'Использовать нейросети для упрощения задач',
        ),
        points=(
            (Study.business, Study.marketing),
            (Study.web, Study.smm),
            (Study.smm, Study.communication),
            (Study.ai, Study.marketing),
        )
    ),
    Question(
        question='<b>Какая роль тебе ближе?</b> 🔎',
        answers=(
            'Организатор — собрать команду, распределить задачи',
            'Идейный вдохновитель — упаковывать и доносить идеи',
            'Тихий стратег — анализировать, предлагать решения',
        ),
        points=(
            (Study.event, Study.business),
            (Study.smm, Study.communication),
            (Study.marketing, Study.ai),
        )
    ),
    Question(
        question='<b>С чего ты начнёшь работу над проектом?</b> 🚀',
        answers=(
            'Узнаю, кто ЦА и как им продать идею',
            'Нарисую визуал и подумаю о стиле',
            'Разложу всё по этапам и организую процесс',
        ),
        points=(
            (Study.marketing, Study.communication),
            (Study.web, Study.smm),
            (Study.business, Study.event),
        )
    ),
    Question(
        question='<b>Что тебе ближе по темпераменту?</b> 🎯',
        answers=(
            'Логика, чёткость, работа с цифрами',
            'Эмоции, яркость, общение с людьми',
            'Визуальное мышление, композиция',
        ),
        points=(
            (Study.ai, Study.marketing, Study.business),
            (Study.smm, Study.communication, Study.event),
            (Study.web, Study.smm),
        )
    ),
    Question(
        question='<b>Что вдохновляет больше?</b> 🏅',
        answers=(
            'Упорядочить хаос и собрать процесс «под ключ»',
            'Сделать проект, которым можно делиться в соцсетях',
            'Понять, как работает система, и улучшить её',
        ),
        points=(
            (Study.business, Study.event),
            (Study.smm, Study.web, Study.communication),
            (Study.ai, Study.marketing),
        )
    ),
    Question(
        question='<b>Представь: презентация проекта. Твоя зона ответственности?</b> 🖇️',
        answers=(
            'Выступаю, убеждаю, договариваюсь',
            'Показываю макеты, визуальные решения',
            'Анализирую метрики и стратегию',
        ),
        points=(
            (Study.communication, Study.event, Study.marketing),
            (Study.smm, Study.web),
            (Study.ai, Study.marketing),
        )
    ),
    Question(
        question='<b>Что важнее всего в работе?</b> 🤍',
        answers=(
            'Осмысленность и возможность расти',
            'Творческая реализация',
            'Возможность изучать новое и делать «умную» работу',
        ),
        points=(
            (Study.business, Study.event, Study.marketing),
            (Study.smm, Study.web, Study.communication),
            (Study.ai, Study.marketing),
        )
    )
)
