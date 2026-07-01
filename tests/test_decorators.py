"""
Тесты для декоратора log.
"""

import os
import pytest
from src.decorators import log


@log()
def success_func(a: int, b: int) -> int:
    """Успешная функция."""
    return a + b


@log()
def error_func(a: int, b: int) -> int:
    """Функция, выбрасывающая ошибку."""
    raise ValueError("Тестовая ошибка")


@log(filename="test_log.txt")
def success_file_func(a: int, b: int) -> int:
    """Успешная функция с записью в файл."""
    return a + b


@log(filename="test_log.txt")
def error_file_func(a: int, b: int) -> int:
    """Функция с ошибкой и записью в файл."""
    raise ValueError("Тестовая ошибка")


def test_log_success_console(capsys):
    """Тест логирования успешного вызова в консоль."""
    success_func(1, 2)
    captured = capsys.readouterr()
    assert "success_func ok" in captured.out


def test_log_error_console(capsys):
    """Тест логирования ошибки в консоль."""
    with pytest.raises(ValueError):
        error_func(1, 2)
    captured = capsys.readouterr()
    assert "error_func error: ValueError" in captured.out


def test_log_success_file():
    """Тест логирования успешного вызова в файл."""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
    success_file_func(3, 4)
    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "success_file_func ok" in content
    os.remove("test_log.txt")


def test_log_error_file():
    """Тест логирования ошибки в файл."""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
    with pytest.raises(ValueError):
        error_file_func(5, 6)
    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert "error_file_func error: ValueError" in content
    os.remove("test_log.txt")
