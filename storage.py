"""Менеджер хранилища данных (JSON)."""
import json
import os
from typing import List, Dict, Any
from models.podcast import Podcast
from models.review import Review
from models.user import User


class StorageManager:
    """Загружает и сохраняет данные в JSON-файлы."""

    def __init__(self, data_dir: str = "data") -> None:
        self.data_dir: str = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def _get_file_path(self, filename: str) -> str:
        """Получить полный путь к файлу в директории данных."""
        return os.path.join(self.data_dir, filename)

    def load_json(self, filename: str) -> List[Dict[str, Any]]:
        """Загрузить список словарей из JSON-файла."""
        filepath = self._get_file_path(filename)
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка чтения {filename}: {e}")
            return []

    def save_json(self, filename: str, data: List[Dict[str, Any]]) -> bool:
        """Сохранить список словарей в JSON-файл."""
        filepath = self._get_file_path(filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except IOError as e:
            print(f"Ошибка записи {filename}: {e}")
            return False

    # === Методы класса (для тестов ПР3 и консольной версии) ===
    # Возвращают сырые списки словарей

    def load_users(self) -> List[Dict[str, Any]]:
        return self.load_json("users.json")

    def load_podcasts(self) -> List[Dict[str, Any]]:
        return self.load_json("podcasts.json")

    def load_reviews(self) -> List[Dict[str, Any]]:
        return self.load_json("reviews.json")

    def save_users(self, users: List[Dict[str, Any]]) -> bool:
        return self.save_json("users.json", users)

    def save_podcasts(self, podcasts: List[Dict[str, Any]]) -> bool:
        return self.save_json("podcasts.json", podcasts)

    def save_reviews(self, reviews: List[Dict[str, Any]]) -> bool:
        return self.save_json("reviews.json", reviews)


# =====================================================================
# СВОБОДНЫЕ ФУНКЦИИ МОДУЛЯ (для Django views)
# =====================================================================
# Возвращают готовые объекты предметной области.
# Импортируются как: from storage import load_podcasts

def load_podcasts(filepath: str = "data/podcasts.json") -> List[Podcast]:
    data_dir = os.path.dirname(filepath) or "data"
    filename = os.path.basename(filepath)
    storage = StorageManager(data_dir=data_dir)
    data = storage.load_json(filename)
    return [Podcast.from_data(item) for item in data]


def load_reviews(filepath: str = "data/reviews.json") -> List[Review]:
    data_dir = os.path.dirname(filepath) or "data"
    filename = os.path.basename(filepath)
    storage = StorageManager(data_dir=data_dir)
    data = storage.load_json(filename)
    return [Review.from_data(item) for item in data]


def load_users(filepath: str = "data/users.json") -> List[User]:
    data_dir = os.path.dirname(filepath) or "data"
    filename = os.path.basename(filepath)
    storage = StorageManager(data_dir=data_dir)
    data = storage.load_json(filename)
    return [User.from_data(item) for item in data]


def save_podcasts(podcasts: List[Podcast], filepath: str = "data/podcasts.json") -> bool:
    data_dir = os.path.dirname(filepath) or "data"
    filename = os.path.basename(filepath)
    storage = StorageManager(data_dir=data_dir)
    data = [p.to_dict() for p in podcasts]
    return storage.save_json(filename, data)


def save_reviews(reviews: List[Review], filepath: str = "data/reviews.json") -> bool:
    data_dir = os.path.dirname(filepath) or "data"
    filename = os.path.basename(filepath)
    storage = StorageManager(data_dir=data_dir)
    data = [r.to_dict() for r in reviews]
    return storage.save_json(filename, data)


def save_users(users: List[User], filepath: str = "data/users.json") -> bool:
    data_dir = os.path.dirname(filepath) or "data"
    filename = os.path.basename(filepath)
    storage = StorageManager(data_dir=data_dir)
    data = [u.to_dict() for u in users]
    return storage.save_json(filename, data)