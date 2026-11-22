from podcasts.models import Podcast
from reviews.models import Review

def global_podcast_stats(request):
    """
    Контекстный процессор, передающий общую статистику
    во все шаблоны, использующие RequestContext.
    """
    return {
        'total_podcasts': Podcast.objects.count(),
        'total_reviews': Review.objects.count(),
    }