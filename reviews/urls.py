from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.reviews_list, name="list"),
    # Статический маршрут "statistics/" должен стоять ДО динамического <int:review_id>/
    path("statistics/", views.statistics, name="statistics"),
    path("create/", views.review_create, name="create"),
    path("<int:review_id>/", views.review_detail, name="detail"),
    path("<int:review_id>/edit/", views.review_update, name="update"),
    path("<int:review_id>/delete/", views.review_delete, name="delete"),
]