from django.db import models

from podcasts.models import Podcast
from users.models import User


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

    class Meta:
        ordering = ["-created_at", "pk"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        rating = f"{self.rating}/5" if self.rating is not None else "без оценки"
        return f"{self.podcast.title} — {rating} ({self.user.username})"