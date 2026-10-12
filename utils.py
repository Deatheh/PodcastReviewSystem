"""Вспомогательные функции ввода."""


def input_int(prompt: str) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное целое число.")


def input_non_empty_string(prompt: str, min_length: int = 1) -> str:
    """Безопасный ввод непустой строки."""
    while True:
        value = input(prompt).strip()
        if len(value) >= min_length:
            return value
        print(f"Ошибка: введите минимум {min_length} символов.")


def input_email(prompt: str) -> str:
    """Безопасный ввод email."""
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email:
            return email
        print("Ошибка: введите корректный email (пример: user@example.com)")