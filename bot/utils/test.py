class Question:
    def __init__(
            self,
            question: str,
            answers: list[str],
            scores: list[int],
    ):
        self.question = question
        self.answers = answers
        self.scores = scores

    def to_text(self, number: int) -> str:
        answers = '\n'.join([f'{i}) {answer}' for i, answer in enumerate(self.answers, 1)])
        return f'{number}. {self.question}\n{answers}'
    
    def get_score(self, answer_number: int) -> int:
        if answer_number not in range(len(self.scores)):
            raise ValueError(f'Номер ответа {answer_number} не найден в списке ответов.')
        return self.scores[answer_number]


question1 = Question(
    question='Какие задачи вам интереснее решать?',
    answers=[
        'Планирование и управление проектами',
        'Создание уникальных визуальных решений для брендов и продуктов',
    ],
    scores=[1, 2]
)
question2 = Question(
    question='Что тебе кажется более увлекательным в рамках учебной или профессиональной деятельности?',
    answers=[
        'Разработка рекламных кампаний',
        'Анализ рынка и поиск интересных идей для бизнеса'
    ],
    scores=[2, 1]
)
question3 = Question(
    question='Что вам интересно больше в будущем?',
    answers=[
        'Работа в крупной компании или собственный бизнес',
        'Креативная работа в агентствах или фриланс'
    ],
    scores=[1, 2]
)
question4 = Question(
    question='Как бы вы описали свой идеальный проект?',
    answers=[
        'Проект, который требует хорошего управления, организации и планирования',
        'Проект, где я могу использовать свою креативность и навыки в графическом дизайне'
    ],
    scores=[1, 2]
)
question5 = Question(
    question='В чем вы видите свои сильные стороны?',
    answers=[
        'Логика, планирование, ответственность за результат',
        'Творческий подход, внимание к деталям, визуальное восприятие'
    ],
    scores=[1, 2]
)

questions = [
    question1,
    question2,
    question3,
    question4,
    question5
]
