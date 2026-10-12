from django.http import HttpResponse
from homepage.views import page
from storage import load_reviews
from models.review import find_review_by_id


def reviews_list(request):
    """Страница списка всех отзывов."""
    reviews_list_data = load_reviews("data/reviews.json")

    items = ""
    for review in reviews_list_data:
        items += f"""
        <li class="list-group-item d-flex justify-content-between align-items-center">
            <div>
                <strong>Отзыв №{review.review_id}</strong>
                <br>
                <small class="text-muted">
                    Подкаст ID: {review.podcast_id}, Пользователь ID: {review.user_id}
                </small>
            </div>
            <a href="/reviews/{review.review_id}/" class="btn btn-sm btn-outline-primary">
                Подробнее
            </a>
        </li>
        """

    content = f"""
    <h1>Отзывы</h1>
    <p class="lead">Всего отзывов: {len(reviews_list_data)}</p>
    <ul class="list-group">
        {items}
    </ul>
    """
    return HttpResponse(page("Список отзывов", content))


def review_detail(request, review_id):
    """Страница конкретного отзыва."""
    reviews_list_data = load_reviews("data/reviews.json")
    review = find_review_by_id(reviews_list_data, review_id)

    if review is None:
        content = """
        <h1 class="text-danger">Отзыв не найден</h1>
        <p>Отзыв с указанным идентификатором не существует.</p>
        <a href="/reviews/" class="btn btn-outline-secondary">← к списку отзывов</a>
        """
        return HttpResponse(page("Отзыв не найден", content), status=404)

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Отзыв №{review.review_id}</h5>
            <p class="card-text"><strong>Подкаст ID:</strong> {review.podcast_id}</p>
            <p class="card-text"><strong>Пользователь ID:</strong> {review.user_id}</p>
            <p class="card-text"><strong>Текст:</strong> {review.text}</p>
            <a href="/reviews/" class="btn btn-outline-secondary">← к списку отзывов</a>
        </div>
    </div>
    """
    return HttpResponse(page(f"Отзыв №{review.review_id}", content), status=200)