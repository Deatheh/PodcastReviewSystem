from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.reviews_list, name="reviews_list"),
    path("<int:review_id>/", views.review_detail, name="review_detail"),
]