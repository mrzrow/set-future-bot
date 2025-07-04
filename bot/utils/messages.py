from .study_enum import Study

START_MESSAGE = '''Привет! Этот бот будет твоим помощником на старте обучения.
Воспользовавшись им, ты сможешь найти ответы на свои вопросы и также пройти тест на выбор курса обучения!'''

QA_MESSAGE = '''<b>1. Ориентированы ли курсы на подготовку с нуля (без образования и диплома)?</b>
Да. Курсы рассчитаны на начинающих. Мы всё объясняем простым языком и сопровождаем участников на каждом этапе.

2. <b>В каком формате проходят занятия?</b>
Все занятия проходят онлайн в малых группах. Это удобно, гибко и позволяет совмещать обучение с учебной нагрузкой.

3. <b>Сколько длится обучение?</b>
Средняя длительность — 2 месяца. График зависит от выбранного направления и собравшейся группы.

4. <b>Есть ли документы об окончании курса?</b>
Да, вы получите именной сертификат, а также доступ к материалам и портфолио выполненных заданий.

5. <b>Помогаете ли вы с трудоустройством?</b>
Да, мы подсказываем, где искать первые заказы, как составить резюме, и поддерживаем ребят на их пути.

6. <b>Смогу ли я применить знания на практике?</b>
Практика — основа наших программ. У каждого модуля есть задания, направленные на реальные кейсы.

7. <b>Когда я смогу начать зарабатывать после курса?</b>
Уже во время обучения ты начнёшь собирать портфолио и получать первые задания. Многие наши ученики берут первые заказы ещё до окончания курса.

8. <b>Можно ли сначала просто узнать подробнее, не покупая курс?</b>
Конечно. Оставьте заявку или напишите нам — мы проконсультируем вас и подскажем, подходит ли программа.'''

COURSES_MESSAGE = '''<b>Бизнес-направление</b> 🧑‍💻
Практический курс для тех, кто хочет разобраться, как устроена компания: деловая переписка, документооборот, основы бухучета и правовых форм, а главное — как эти знания применять на практике.

<b>Веб-дизайн</b> 🗂️
Курс для тех, кто хочет войти в IT без программирования. Работаем в Figma, Tilda и других инструментах, учимся делать удобные и красивые интерфейсы под реальные задачи бизнеса.

<b>SMM и контент-мейкинг</b> 📝
Учитесь создавать визуалы, писать посты, снимать и монтировать видео, оформлять соцсети и выстраивать личный бренд — всё, что нужно, чтобы начать карьеру в медиа или продвигать собственный проект.

<b>Искусственный интеллект</b> 🖥️
Погружение в мир нейросетей и цифровых инструментов: разбираем, как они работают, как с ними обращаться, и где можно начать зарабатывать, даже не будучи программистом.

<b>Event-направление</b> 🌠
Организация мероприятий с нуля: учитесь продумывать концепцию, писать сценарии, считать сметы, собирать команды и доводить проекты до результата — как онлайн, так и офлайн.

<b>Маркетинг и анализ рынка</b> 🎯
Разбираемся, как компании изучают потребителей, анализируют рынок и строят стратегии продвижения. Осваиваем Excel, исследуем аудитории, учимся думать как маркетолог.

<b>Коммуникации</b> 📲
Курс о том, как уверенно общаться: вести переговоры, выступать, договариваться, управлять конфликтами и быть убедительным — навыки, которые нужны в любой профессии и жизни.
'''

HELP_MESSAGE = '''За помощью обращайтесь к консультанту: @studyoschool_manager'''

TEST_START_MESSAGE = '''Предлагаем тебе пройти тест на выбор курса обучения! 🤍
Это поможет тебе не ошибиться и изучать то, что тебе интересно! 

Ответы принимаются в виде цифр: 1, 2, 3 или 4
'''

RESULT_MESSAGE = 'Судя по вашим интересам и навыкам, вам могут подойти такие профессии, как:\n{}\n\nА обучится на них вы сможете на нашем курсе «{}». Подробная информация на <a href="https://xn--80aimylg.xn--p1ai/">сайте</a> 🤍'
COURSES_NAMES = {
    Study.business: 'Бизнес-направление: от деловой переписки до первых шагов в карьере',
    Study.marketing: 'Маркетинговое направление: от целевой аудитории до запуска решений',
    Study.web: 'Веб-дизайн: от создания дизайна до сборки сайта',
    Study.smm: 'SMM и контент-мейкинг: от постов до управляемой онлайн-репутации',
    Study.communication: 'Коммуникации: от уверенного общения до управления переговорами',
    Study.ai: 'Искусственный интеллект: от основ до практики в повседневных задачах',
    Study.event: 'Event-направление: от идеи до реализованного события'
}
COURSES_BULLET_POINTS = {
    Study.business: '''<b>
    • начинающий предприниматель
    • бизнес-ассистент
    • личный ассистент
    • помощник руководителя</b>''',
    Study.marketing: '''<b>
    • аналитик начального уровня
    • ассистент маркетолога
    • помощник бренд-менеджера</b>''',
    Study.web: '''<b>
    • дизайнер интерфейсов
    • UX/UI дизайнер
    • WEB-дизайнер
    • графический дизайнер
    • дизайнер презентаций</b>''',
    Study.smm: '''<b>
    • ассистент маркетолога
    • smm-специалист
    • контент-мейкер
    • автор медиа проектов
    • администратор соцсетей</b>''',
    Study.communication: '''<b>
    • организатор деловых коммуникаций
    • ассистент в команде
    • представитель на переговорах</b>''',
    Study.ai: '''<b>
    • контент-мейкер с ИИ-усилением
    • AI-художник
    • помощник в digital-командах
    • промпт-дизайнер</b>''',
    Study.event: '''<b>
    • координатор мероприятий
    • организатор событий
    • ассистент event-менеджера</b>''',
}
