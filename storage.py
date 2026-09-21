import json
import os
from typing import List, Dict, Any


def load_podcasts(filename: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Ошибка: некорректный формат JSON в файле {filename}")
        return []


def save_podcasts(filename: str, podcasts: List[Dict[str, Any]]) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(podcasts, f, ensure_ascii=False, indent=4)


def load_reviews(filename: str) -> List[Dict[str, Any]]:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Ошибка: некорректный формат JSON в файле {filename}")
        return []


def save_reviews(filename: str, reviews: List[Dict[str, Any]]) -> None:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(reviews, f, ensure_ascii=False, indent=4)
