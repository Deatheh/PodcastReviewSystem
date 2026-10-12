from django.http import HttpResponse
from homepage.views import page
from storage import load_podcasts
from models.podcast import find_podcast_by_id


def podcasts_list(request):
    """Страница списка всех подкастов."""
    podcasts_list = load_podcasts("data/podcasts.json")

    items = ""
    for podcast in podcasts_list:
        items += f"""
        <li class="list-group-item d-flex justify-content-between align-items-center">
            <div>
                <strong>{podcast.title}</strong>
                <br>
                <small class="text-muted">ID: {podcast.podcast_id}</small>
            </div>
            <a href="/podcasts/{podcast.podcast_id}/" class="btn btn-sm btn-outline-primary">
                Подробнее
            </a>
        </li>
        """

    content = f"""
    <h1>Подкасты</h1>
    <p class="lead">Всего подкастов: {len(podcasts_list)}</p>
    <ul class="list-group">
        {items}
    </ul>
    """
    return HttpResponse(page("Список подкастов", content))


def podcast_detail(request, podcast_id):
    """Страница конкретного подкаста."""
    podcasts_list = load_podcasts("data/podcasts.json")
    podcast = find_podcast_by_id(podcasts_list, podcast_id)

    if podcast is None:
        content = """
        <h1 class="text-danger">Подкаст не найден</h1>
        <p>Подкаст с указанным идентификатором не существует.</p>
        <a href="/podcasts/" class="btn btn-outline-secondary">← к списку подкастов</a>
        """
        return HttpResponse(page("Подкаст не найден", content), status=404)

    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{podcast.title}</h5>
            <p class="card-text"><strong>ID:</strong> {podcast.podcast_id}</p>
            <p class="card-text"><strong>Автор ID:</strong> {podcast.author_id or 'не указан'}</p>
            <a href="/podcasts/" class="btn btn-outline-secondary">← к списку подкастов</a>
        </div>
    </div>
    """
    return HttpResponse(page(podcast.title, content), status=200)