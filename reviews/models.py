from django.db import models
from podcasts.models import Podcast
from users.models import User

# 1. Создаем кастомный QuerySet
class ReviewQuerySet(models.QuerySet):
    def with_rating(self):
        """Возвращает только отзывы, где есть оценка."""
        return self.filter(rating__isnull=False)

    def without_rating(self):
        """Возвращает отзывы без оценки."""
        return self.filter(rating__isnull=True)


# 2. Создаем менеджер на основе этого QuerySet
class ReviewManager(models.Manager.from_queryset(ReviewQuerySet)):
    pass


class Review(models.Model):
    """Отзыв пользователя о подкасте."""

    podcast = models.ForeignKey(
        Podcast,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Подкаст",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Пользователь",
    )
    text = models.TextField(
        blank=True,
        default="",
        verbose_name="Текст отзыва",
    )
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Оценка",
        help_text="Целое число от 1 до 5; может отсутствовать в исходных данных",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    # 3. Подключаем наш кастомный менеджер
    objects = ReviewManager()

    class Meta:
        ordering = ["-created_at", "pk"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        rating_str = f"{self.rating}/5" if self.rating is not None else "без оценки"
        return f"{self.podcast.title} — {rating_str} ({self.user.username})"