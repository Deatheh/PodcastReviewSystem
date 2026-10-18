from django.shortcuts import render
from storage import load_podcasts
from models.podcast import find_podcast_by_id


def podcasts_list(request):
    podcasts_data = load_podcasts("data/podcasts.json")
    context = {
        "podcasts": podcasts_data,
    }
    return render(request, "podcasts/podcast_list.html", context)


def podcast_detail(request, podcast_id):
    podcasts_data = load_podcasts("data/podcasts.json")
    podcast = find_podcast_by_id(podcasts_data, podcast_id)

    context = {
        "podcast": podcast,
    }
    return render(request, "podcasts/podcast_detail.html", context, status=404 if podcast is None else 200)