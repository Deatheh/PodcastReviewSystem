from django.http import HttpResponse

def page(title, content):
    bootstrap = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    return f"""<!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{title}</title>
        <link rel="stylesheet" href="{bootstrap}">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light mb-4">
            <div class="container">
                <a class="navbar-brand" href="/">PodcastReview</a>
                <div class="navbar-nav">
                    <a class="nav-link" href="/podcasts/">Подкасты</a>
                    <a class="nav-link" href="/reviews/">Отзывы</a>
                </div>
            </div>
        </nav>
        <main class="container">{content}</main>
    </body>
    </html>"""

def index(request):
    content = """
    <h1 class="display-4">Система отзывов о подкастах</h1>
    <p class="lead">Добро пожаловать! Выберите раздел:</p>
    <a href="/podcasts/" class="btn btn-primary me-2">Список подкастов</a>
    <a href="/reviews/" class="btn btn-secondary">Список отзывов</a>
    """
    return HttpResponse(page("Главная", content))

def page_not_found(request, exception):
    content = """
    <h1 class="text-danger">404 – страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(page("404", content), status=404)