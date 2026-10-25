from django.urls import path
from . import views

# Вот эта строчка связывает приложение с namespace!
app_name = "podcasts"

urlpatterns = [
    path("", views.podcasts_list, name="list"), # name="list" создает имя 'podcasts:list'
    path("search/", views.podcasts_search, name="search"),
    path("<int:podcast_id>/", views.podcast_detail, name="detail"),
]