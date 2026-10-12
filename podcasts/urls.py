from django.urls import path
from . import views
urlpatterns = [
    path("", views.podcasts_list, name="podcasts_list"),
    path("<int:podcast_id>/", views.podcast_detail, name="podcast_detail"),
]