from django.contrib import admin
from django.urls import include, path

handler404 = "homepage.views.page_not_found" # Для критерия 21

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("podcasts/", include("podcasts.urls")),
    path("reviews/", include("reviews.urls")),
]