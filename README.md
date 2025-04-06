SQL-like Query Parser

Проект представляет собой парсер SQL-подобных запросов с оптимизатором для гипотетической NoSQL-системы.

Технологии

- Python 3.12+ - Основной язык реализации
- Parsimonious - PEG-парсер для разбора запросов
- Pydantic v2 - Валидация данных и построение AST
- pytest - Тестирование компонентов
- Numba (опционально) - JIT-оптимизация критичных участков
- *ype Hints - Полная статическая типизация проекта

Особенности

- Полноценный парсер SQL-подобного синтаксиса
- Построение типизированного AST
- Оптимизация запросов (удаление бесполезных условий)
- Профессиональная организация кода:
  - Разделение грамматики и логики парсера
  - Чёткое разделение слоёв (парсинг → AST → оптимизация)
  - Полное покрытие тестами

Установка

1. Клонировать репозиторий:
git clone https://github.com/yourusername/sql-parser.git
cd sql-parser

2. Установить зависимости:     pip install -e .

Запуск тестов:    pytest tests/ -v


sql_parser/
├── core/               # Основная логика
│   ├── parser.py       # Парсер запросов
│   ├── ast_models.py   # Модели AST (Pydantic)
│   ├── optimizer.py    # Логика оптимизации
│   └── exceptions.py   # Кастомные ошибки
├── grammar/            # PEG-грамматика
├── tests/              # Юнит-тесты
└── scripts/            # Вспомогательные скрипты

Дальнейшее развитие
Поддержка JOIN и вложенных запросов
Генерация кода для конкретных СУБД
Интеграция с IDE через LSP-сервер
Бенчмаркинг производительности
