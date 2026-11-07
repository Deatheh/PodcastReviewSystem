from django.core.paginator import Paginator
from django.db.models import Avg, Count, Q
from django.shortcuts import get_object_or_404, render

from .models import Review
from podcasts.models import Podcast
from users.models import User

def reviews_list(request):
    """Список отзывов с фильтрацией, сортировкой и пагинацией."""
    reviews_qs = Review.objects.select_related("podcast", "user").all()

    # 1. Фильтрация
    rating = request.GET.get("rating", "").strip()
    podcast_id = request.GET.get("podcast", "").strip()
    user_id = request.GET.get("user", "").strip()

    if rating.isdigit():
        reviews_qs = reviews_qs.filter(rating=int(rating))
    if podcast_id.isdigit():
        reviews_qs = reviews_qs.filter(podcast_id=int(podcast_id))
    if user_id.isdigit():
        reviews_qs = reviews_qs.filter(user_id=int(user_id))

    # 2. Сортировка
    sort = request.GET.get("sort", "-created_at")
    allowed_sort = {
        "-created_at": "-created_at",
        "created_at": "created_at",
        "-rating": "-rating",
        "rating": "rating",
        "podcast": "podcast__title",
        "user": "user__username",
    }
    sort_field = allowed_sort.get(sort, "-created_at")
    reviews_qs = reviews_qs.order_by(sort_field, "pk")

    # 3. Пагинация (по 5 записей на страницу)
    paginator = Paginator(reviews_qs, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page_obj,
        "reviews": page_obj,
        "podcasts": Podcast.objects.order_by("title"),
        "users": User.objects.order_by("username"),
        "selected_rating": rating,
        "selected_podcast": podcast_id,
        "selected_user": user_id,
        "sort": sort,
    }
    return render(request, "reviews/review_list.html", context)

def review_detail(request, review_id):
    """Детальная страница отзыва."""
    review = get_object_or_404(
        Review.objects.select_related("podcast", "user"),
        pk=review_id,
    )
    return render(request, "reviews/review_detail.html", {"review": review})

def statistics(request):
    """Статистика: количество отзывов и средний рейтинг по подкастам."""
    # Используем annotate для подсчета связанных объектов
    stats = (
        Podcast.objects.annotate(
            reviews_count=Count("reviews"),
            avg_rating=Avg("reviews__rating"),
        )
        .order_by("-reviews_count", "title")
    )

    context = {
        "stats": stats,
        "total_reviews": Review.objects.count(),
        "total_podcasts": Podcast.objects.count(),
    }
    return render(request, "reviews/statistics.html", context)