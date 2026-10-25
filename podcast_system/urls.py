from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Вот здесь ОБЯЗАТЕЛЬНО должен быть namespace
    path('podcasts/', include('podcasts.urls', namespace='podcasts')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('', include('homepage.urls', namespace='homepage')),
]

handler404 = "homepage.views.page_not_found"