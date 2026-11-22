from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Avg, Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from podcasts.models import Podcast

from .forms import ReviewFilterForm, ReviewForm
from .models import Review


def reviews_list(request):
    """Список отзывов с фильтрацией через форму (GET) и пагинацией."""
    filter_form = ReviewFilterForm(request.GET or None)
    form_valid = filter_form.is_bound and filter_form.is_valid()

    # Оптимизация N+1 из ПР10
    reviews_qs = Review.objects.select_related("podcast", "user").all()

    # Применяем фильтры только если форма прошла валидацию
    if form_valid:
        podcast = filter_form.cleaned_data.get("podcast")
        min_rating = filter_form.cleaned_data.get("min_rating")
        if podcast:
            reviews_qs = reviews_qs.filter(podcast=podcast)
        if min_rating:
            reviews_qs = reviews_qs.filter(rating__gte=min_rating)

    reviews_qs = reviews_qs.order_by("-created_at")

    paginator = Paginator(reviews_qs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "reviews": page_obj,
        "page_obj": page_obj,
        "filter_form": filter_form,
    }
    return render(request, "reviews/reviews_list.html", context)


def review_detail(request, review_id):
    """Детальная страница отзыва."""
    review = get_object_or_404(
        Review.objects.select_related("podcast", "user"),
        pk=review_id,
    )
    context = {"review": review}
    return render(request, "reviews/review_detail.html", context)


def statistics(request):
    """Статистика: общие показатели + разбивка по подкастам (как в ПР9)."""
    # Агрегация по всем отзывам
    overall = Review.objects.aggregate(
        total_reviews=Count("id"),
        with_rating=Count("id", filter=Q(rating__isnull=False)),
        without_rating=Count("id", filter=Q(rating__isnull=True)),
    )

    # Статистика по каждому подкасту (включая подкасты без отзывов)
    podcast_stats = (
        Podcast.objects
        .annotate(
            reviews_count=Count("reviews"),
            avg_rating=Avg("reviews__rating"),
        )
        .order_by("-reviews_count", "title")
    )

    context = {
        "overall": overall,
        "podcast_stats": podcast_stats,
    }
    return render(request, "reviews/statistics.html", context)


def review_create(request):
    """Создание нового отзыва через ModelForm."""
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, "Отзыв успешно создан!")
            return redirect("reviews:detail", review_id=review.pk)
    else:
        form = ReviewForm()

    context = {"form": form, "action": "Создание отзыва"}
    return render(request, "reviews/review_form.html", context)


def review_update(request, review_id):
    """Редактирование существующего отзыва (instance)."""
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Отзыв успешно обновлён!")
            return redirect("reviews:detail", review_id=review.pk)
    else:
        form = ReviewForm(instance=review)

    context = {"form": form, "action": "Редактирование отзыва", "review": review}
    return render(request, "reviews/review_form.html", context)


@require_POST
def review_delete(request, review_id):
    """Удаление отзыва (только POST, защита от GET-удаления)."""
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, "Отзыв удалён.")
    return redirect("reviews:list")