from src.utils import read_transactions_from_json

# Вызов функции для проверки логирования
data = read_transactions_from_json("data/operations.json")
print(data)