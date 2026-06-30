\# Виджет банковских операций



Проект для фильтрации и сортировки списка банковских транзакций.



\## Установка



```bash

git clone https://github.com/твой-логин/bank\_widget.git

cd bank\_widget

```



\## Зависимости



Для работы проекта необходимы:

\- Python 3.12+

\- Poetry (для управления зависимостями)



Установка Poetry:

```bash

pip install poetry

```



Установка линтеров для проверки кода:

```bash

pip install flake8 mypy black isort

```



\## Использование



```python

from src.processing import filter\_by\_state, sort\_by\_date



data = \[

&#x20;   {'id': 1, 'state': 'EXECUTED', 'date': '2025-01-01'},

&#x20;   {'id': 2, 'state': 'CANCELED', 'date': '2024-12-01'},

]



executed = filter\_by\_state(data)

sorted\_data = sort\_by\_date(data)

```



\## Функции



\- `filter\_by\_state(transactions, state='EXECUTED')` — фильтрует транзакции по статусу.

\- `sort\_by\_date(transactions, descending=True)` — сортирует транзакции по дате.



\## Проверка кода



Запуск проверок:

```bash

flake8 src/

mypy src/

black src/

isort src/

```

## Тестирование

Для запуска тестов выполните команду:

```bash
pytest

Для получения отчёта о покрытии:

bash
pytest --cov=src --cov-report=html
