from django.contrib import admin
from .models import User
from reviews.models import Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    fields = ("podcast", "rating", "text", "created_at")
    readonly_fields = ("created_at",)
    can_delete = False

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    list_display_links = ("username",)
    search_fields = ("username", "email")
    ordering = ("username",)
    list_per_page = 20
    inlines = (ReviewInline,)