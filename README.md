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

## Чтение CSV и Excel

Модуль `file_processing` позволяет читать транзакции из CSV и Excel файлов.

```python
from src.file_processing import read_transactions_from_csv, read_transactions_from_excel

csv_data = read_transactions_from_csv("data/transactions.csv")
excel_data = read_transactions_from_excel("data/transactions_excel.xlsx")