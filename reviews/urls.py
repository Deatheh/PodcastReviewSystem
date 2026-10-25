from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.reviews_list, name="list"),
    path("statistics/", views.statistics, name="statistics"),
    path("<int:review_id>/", views.review_detail, name="detail"),
]