"""Модель подкаста."""
from typing import Dict, Any, Optional


class Podcast:
    """Подкаст, доступный для прослушивания и оценки."""

    def __init__(
        self,
        podcast_id: int,
        title: str,
        author_id: Optional[int] = None,
    ) -> None:
        self.podcast_id: int = podcast_id
        self.title: str = title
        self.author_id: Optional[int] = author_id

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "Podcast":
        """Создать объект Podcast из словаря (например, из JSON)."""
        return cls(
            podcast_id=data["podcast_id"],
            title=data["title"],
            author_id=data.get("author_id"),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразовать объект в словарь для сохранения в JSON."""
        return {
            "podcast_id": self.podcast_id,
            "title": self.title,
            "author_id": self.author_id,
        }

    def matches_title(self, query: str) -> bool:
        """Проверить, совпадает ли название с поисковым запросом."""
        return query.strip().lower() in self.title.lower()

    def __str__(self) -> str:
        author_info = f", author_id={self.author_id}" if self.author_id else ""
        return f"Podcast(id={self.podcast_id}, title='{self.title}'{author_info})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Podcast):
            return False
        return (
            self.podcast_id == other.podcast_id
            and self.title.lower() == other.title.lower()
        )