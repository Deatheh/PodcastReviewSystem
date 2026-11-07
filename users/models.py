from django.db import models


class User(models.Model):
    """Пользователь системы, оставляющий отзывы."""

    username = models.CharField(
        max_length=150,
        verbose_name="Имя пользователя",
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username