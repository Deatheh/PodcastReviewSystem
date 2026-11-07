from django.db import models


class Podcast(models.Model):
    """Подкаст, доступный для прослушивания и оценки."""

    title = models.CharField(
        max_length=255,
        verbose_name="Название подкаста",
    )
    author_id = models.PositiveIntegerField(
        null=True,          # <-- разрешаем NULL в БД
        blank=True,         # <-- разрешаем пустое значение в формах/админке
        verbose_name="ID автора",
        help_text="Идентификатор автора из исходной базы (может отсутствовать)",
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "Подкаст"
        verbose_name_plural = "Подкасты"

    def __str__(self):
        return self.title