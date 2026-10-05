"""Менеджер хранилища данных (JSON)."""
import json
import os
from typing import List, Dict, Any


class StorageManager:
    """Загружает и сохраняет данные в JSON-файлы."""

    def __init__(self, data_dir: str = "data") -> None:
        self.data_dir: str = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def _get_file_path(self, filename: str) -> str:
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

    def load_users(self) -> List[Dict[str, Any]]:
        return self.load_json("users.json")

    def save_users(self, users: List[Dict[str, Any]]) -> bool:
        return self.save_json("users.json", users)

    def load_podcasts(self) -> List[Dict[str, Any]]:
        return self.load_json("podcasts.json")

    def save_podcasts(self, podcasts: List[Dict[str, Any]]) -> bool:
        return self.save_json("podcasts.json", podcasts)

    def load_reviews(self) -> List[Dict[str, Any]]:
        return self.load_json("reviews.json")

    def save_reviews(self, reviews: List[Dict[str, Any]]) -> bool:
        return self.save_json("reviews.json", reviews)