"""Модель отзыва."""
from typing import Dict, Any


class Review:
    """Отзыв пользователя о подкасте."""

    def __init__(
        self,
        review_id: int,
        podcast_id: int,
        user_id: int,
        text: str,
    ) -> None:
        self.review_id: int = review_id
        self.podcast_id: int = podcast_id
        self.user_id: int = user_id
        self.text: str = text

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "Review":
        """Создать объект Review из словаря."""
        return cls(
            review_id=data["review_id"],
            podcast_id=data["podcast_id"],
            user_id=data["user_id"],
            text=data["text"],
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразовать объект в словарь для JSON."""
        return {
            "review_id": self.review_id,
            "podcast_id": self.podcast_id,
            "user_id": self.user_id,
            "text": self.text,
        }

    def __str__(self) -> str:
        return (
            f"Review(id={self.review_id}, podcast_id={self.podcast_id}, "
            f"user_id={self.user_id}, text='{self.text}')"
        )

    def __repr__(self) -> str:
        return self.__str__()