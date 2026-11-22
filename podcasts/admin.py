from django.contrib import admin
from .models import Podcast
from reviews.models import Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    fields = ("user", "rating", "text", "created_at")
    readonly_fields = ("created_at",)
    can_delete = False  # Запрещаем удалять историю отзывов из карточки подкаста

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author_id")
    list_display_links = ("title",)
    search_fields = ("title",)
    ordering = ("title",)
    list_per_page = 20
    inlines = (ReviewInline,)
    view_on_site = True  # Включает кнопку "Смотреть на сайте" благодаря get_absolute_url