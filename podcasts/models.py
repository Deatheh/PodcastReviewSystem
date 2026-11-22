from django.db import models

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
    # <-- НОВОЕ ПОЛЕ ДЛЯ ПР11
    cover_image = models.ImageField(
        upload_to="podcast_covers/",
        blank=True,
        null=True,
        verbose_name="Обложка подкаста",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Подкаст"
        verbose_name_plural = "Подкасты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('podcasts:detail', kwargs={'podcast_id': self.pk})