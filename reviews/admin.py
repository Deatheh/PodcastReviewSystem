from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "podcast", "user", "rating", "created_at")
    list_display_links = ("id",)
    # Поиск по связанным моделям через двойное подчёркивание
    search_fields = ("podcast__title", "user__username", "text")
    list_filter = ("rating", "created_at")
    ordering = ("-created_at",)
    list_per_page = 20
    readonly_fields = ("created_at",)