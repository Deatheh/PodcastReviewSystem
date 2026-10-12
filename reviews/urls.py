from django.urls import path
from . import views


urlpatterns = [
    path("", views.reviews_list, name="reviews_list"),
    path("<int:review_id>/", views.review_detail, name="review_detail"),
]