from django import forms
from django.core.exceptions import ValidationError

from podcasts.models import Podcast
from .models import Review


class ReviewFilterForm(forms.Form):
    """Форма фильтрации списка отзывов (GET-запрос)."""

    podcast = forms.ModelChoiceField(
        queryset=Podcast.objects.order_by("title"),
        required=False,
        label="Подкаст",
        empty_label="Все подкасты",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    min_rating = forms.IntegerField(
        required=False,
        label="Минимальная оценка",
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "От 1 до 5",
            "min": 1,
            "max": 5,
        }),
    )

    def clean_min_rating(self):
        rating = self.cleaned_data.get("min_rating")
        if rating is not None and (rating < 1 or rating > 5):
            raise ValidationError("Оценка должна быть от 1 до 5.")
        return rating


class ReviewForm(forms.ModelForm):
    """Форма создания и редактирования отзыва (ModelForm)."""

    class Meta:
        model = Review
        fields = ["podcast", "user", "text", "rating"]
        labels = {
            "podcast": "Подкаст",
            "user": "Автор отзыва",
            "text": "Текст отзыва",
            "rating": "Оценка (1–5)",
        }
        widgets = {
            "podcast": forms.Select(attrs={"class": "form-select"}),
            "user": forms.Select(attrs={"class": "form-select"}),
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Напишите ваш отзыв...",
            }),
            "rating": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 1,
                "max": 5,
            }),
        }
        help_texts = {
            "rating": "Оставьте пустым, если не хотите ставить оценку.",
        }

    def clean_text(self):
        text = self.cleaned_data.get("text")
        if text and not text.strip():
            raise ValidationError("Текст отзыва не может состоять только из пробелов.")
        return text.strip()

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating is not None and (rating < 1 or rating > 5):
            raise ValidationError("Оценка должна быть целым числом от 1 до 5.")
        return rating