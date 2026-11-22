from django.db import models
from django.urls import reverse  # <-- Добавь этот импорт

class Podcast(models.Model):
    """Подкаст, доступный для прослушивания и оценки."""

    title = models.CharField(
        max_length=255,
        verbose_name="Название подкаста",
    )
    author_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="ID автора",
        help_text="Идентификатор автора из исходной базы (может отсутствовать)",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Подкаст"
        verbose_name_plural = "Подкасты"

    def __str__(self):
        return self.title

    # <-- Добавь этот метод
    def get_absolute_url(self):
        """Возвращает URL детальной страницы подкаста."""
        # Убедись, что в podcasts/urls.py маршрут называется 'detail'
        # и принимает параметр podcast_id
        return reverse('podcasts:detail', kwargs={'podcast_id': self.pk})