\# Виджет банковских операций



Проект для фильтрации и сортировки списка банковских транзакций.



\## Установка



```bash

git clone https://github.com/твой-логин/bank\_widget.git

cd bank\_widget

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

## Модуль decorators

Модуль содержит декоратор `log` для автоматического логирования вызовов функций.

### Декоратор log

Логирует вызов функции: имя, аргументы, результат или ошибку.

```python
from src.decorators import log

@log()
def add(a, b):
    return a + b

add(1, 2)  # выведет в консоль: add ok

@log(filename="log.txt")
def divide(a, b):
    return a / b

divide(10, 0)  # запишет в файл: divide error: ZeroDivisionError. Inputs: (10, 0), {}
Аргументы:

filename (опционально): если указан, логи пишутся в файл, иначе — в консоль.

## Модуль utils

Модуль содержит функцию для чтения данных о транзакциях из JSON-файла.

### read_transactions_from_json(file_path)

Читает JSON-файл и возвращает список транзакций.

```python
from src.utils import read_transactions_from_json

transactions = read_transactions_from_json("data/operations.json")
print(transactions)

Модуль external_api
Модуль содержит функцию для конвертации валют в рубли через внешнее API.

convert_to_rubles(transaction)
Конвертирует сумму транзакции в рубли.

python
from src.external_api import convert_to_rubles

transaction = {
    "operationAmount": {
        "amount": "100.00",
        "currency": {"code": "USD"}
    }
}
result = convert_to_rubles(transaction)
print(result)  # 7500.0 (пример)
Переменные окружения
Для работы с API используется файл .env. Скопируйте .env.example и добавьте свой ключ:

bash
EXCHANGE_RATE_API_KEY=ваш_ключ_от_api
Тестирование
Запуск тестов:

bash
pytest
Отчёт о покрытии:

bash
pytest --cov=src --cov-report=html