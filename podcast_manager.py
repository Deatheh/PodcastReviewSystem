"""Менеджер подкастов."""
from typing import List, Optional, Dict, Any
from podcasts import Podcast


class PodcastManager:
    """Управляет коллекцией подкастов."""

    def __init__(self) -> None:
        self.podcasts: List[Podcast] = []

    def add_podcast(
        self, title: str, author_id: Optional[int] = None
    ) -> Optional[Podcast]:
        """Добавить новый подкаст. Возвращает объект или None при ошибке."""
        clean_title = title.strip()
        if len(clean_title) < 4:
            print("Ошибка: название должно содержать не менее 4 символов!")
            return None
        if any(p.title.lower() == clean_title.lower() for p in self.podcasts):
            print(f"Ошибка: подкаст '{clean_title}' уже существует!")
            return None

        new_id = max((p.podcast_id for p in self.podcasts), default=0) + 1
        new_podcast = Podcast(new_id, clean_title, author_id)
        self.podcasts.append(new_podcast)
        print(f"Подкаст '{clean_title}' успешно добавлен (ID: {new_id})")
        return new_podcast

    def find_by_id(self, podcast_id: int) -> Optional[Podcast]:
        """Найти подкаст по идентификатору."""
        return next(
            (p for p in self.podcasts if p.podcast_id == podcast_id), None
        )

    def find_by_title(self, query: str) -> List[Podcast]:
        """Найти подкасты по части названия."""
        return [p for p in self.podcasts if p.matches_title(query)]

    def get_all(self) -> List[Podcast]:
        """Вернуть копию списка подкастов."""
        return self.podcasts.copy()

    def load_from_list(self, podcasts_data: List[Dict[str, Any]]) -> None:
        """Загрузить подкасты из списка словарей."""
        self.podcasts = [Podcast.from_data(data) for data in podcasts_data]

    def save_to_list(self) -> List[Dict[str, Any]]:
        """Сериализовать подкасты в список словарей."""
        return [podcast.to_dict() for podcast in self.podcasts]