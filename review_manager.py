"""Менеджер отзывов."""
from typing import List, Dict, Any
from reviews import Review
from podcast_manager import PodcastManager


class ReviewManager:
    """Управляет коллекцией отзывов."""

    def __init__(self) -> None:
        self.reviews: List[Review] = []

    def add_review(
        self,
        podcast_id: int,
        user_id: int,
        text: str,
        podcast_manager: PodcastManager,
    ) -> bool:
        """Добавить отзыв к подкасту."""
        podcast = podcast_manager.find_by_id(podcast_id)
        if not podcast:
            print(f"Ошибка: подкаст с ID {podcast_id} не найден!")
            return False

        clean_text = text.strip()
        if len(clean_text) < 1:
            print("Ошибка: текст отзыва не может быть пустым!")
            return False

        new_id = max((r.review_id for r in self.reviews), default=0) + 1
        new_review = Review(new_id, podcast_id, user_id, clean_text)
        self.reviews.append(new_review)
        print(f"Отзыв успешно добавлен к подкасту '{podcast.title}'")
        return True

    def get_for_podcast(self, podcast_id: int) -> List[Review]:
        """Вернуть отзывы о конкретном подкасте."""
        return [r for r in self.reviews if r.podcast_id == podcast_id]

    def get_for_user(self, user_id: int) -> List[Review]:
        """Вернуть отзывы конкретного пользователя."""
        return [r for r in self.reviews if r.user_id == user_id]

    def get_all(self) -> List[Review]:
        """Вернуть копию списка отзывов."""
        return self.reviews.copy()

    def load_from_list(self, reviews_data: List[Dict[str, Any]]) -> None:
        """Загрузить отзывы из списка словарей."""
        self.reviews = [Review.from_data(data) for data in reviews_data]

    def save_to_list(self) -> List[Dict[str, Any]]:
        """Сериализовать отзывы в список словарей."""
        return [review.to_dict() for review in self.reviews]