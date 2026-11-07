from django.shortcuts import get_object_or_404, render
from .models import Podcast
from reviews.models import Review


def podcasts_list(request):
    """Список всех подкастов."""
    podcasts = Podcast.objects.order_by("title")
    return render(request, "podcasts/podcast_list.html", {"podcasts": podcasts})


def podcast_detail(request, podcast_id):
    """Детальная страница подкаста с его отзывами."""
    podcast = get_object_or_404(Podcast, pk=podcast_id)

    # Получаем отзывы для этого подкаста, сразу подгружая пользователей
    reviews = Review.objects.filter(podcast=podcast).select_related("user").order_by("-created_at")

    return render(request, "podcasts/podcast_detail.html", {
        "podcast": podcast,
        "reviews": reviews,
    })


def podcasts_search(request):
    """Поиск подкастов по названию."""
    query = request.GET.get("q", "").strip()
    results = []

    if query:
        results = Podcast.objects.filter(title__icontains=query).order_by("title")

    return render(request, "podcasts/search.html", {
        "query": query,
        "results": results,
    })