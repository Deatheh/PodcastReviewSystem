from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Вот здесь ОБЯЗАТЕЛЬНО должен быть namespace
    path('podcasts/', include('podcasts.urls', namespace='podcasts')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('', include('homepage.urls', namespace='homepage')),
]

handler404 = "homepage.views.page_not_found"

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns