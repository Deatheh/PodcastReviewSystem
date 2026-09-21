def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное целое число.")


def input_non_empty_string(prompt: str, min_length: int = 4) -> str:
    while True:
        value = input(prompt).strip()
        if len(value) >= min_length:
            return value
        print(f"Ошибка: название должно содержать не менее {min_length} симв.")
