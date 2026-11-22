from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from .models import Review


def reviews_list(request):
    """
    Отображает список всех отзывов.
    Оптимизация: select_related загружает связанные podcast и user
    одним запросом, предотвращая N+1 проблему.
    """
    # Полный оптимизированный QuerySet
    reviews = Review.objects.select_related('podcast', 'user').all().order_by('-created_at')

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews_list.html', context)


def review_detail(request, review_id):
    """
    Отображает детальный просмотр одного отзыва.
    Оптимизация: get_object_or_404 с select_related.
    """
    review = get_object_or_404(
        Review.objects.select_related('podcast', 'user'),
        pk=review_id
    )

    context = {
        'review': review,
    }
    return render(request, 'reviews/review_detail.html', context)


def statistics(request):
    """Отображает статистику по отзывам (всего, с оценкой, без оценки)."""
    stats = Review.objects.aggregate(
        total_reviews=Count('id'),
        with_rating=Count('id', filter=Q(rating__isnull=False)),
        without_rating=Count('id', filter=Q(rating__isnull=True)),
    )

    context = {
        'stats': stats,
    }
    # Убедитесь, что у вас создан шаблон reviews/statistics.html!
    return render(request, 'reviews/statistics.html', context)