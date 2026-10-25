from django.shortcuts import render

def index(request):
    # Просто рендерим главную страницу
    return render(request, "homepage/index.html")

def page_not_found(request, exception=None):
    # Рендерим кастомную 404
    return render(request, "homepage/404.html", status=404)