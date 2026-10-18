from django.shortcuts import render
from storage import load_reviews
from models.review import find_review_by_id


def reviews_list(request):
    reviews_data = load_reviews("data/reviews.json")
    context = {
        "reviews": reviews_data,
    }
    return render(request, "reviews/review_list.html", context)


def review_detail(request, review_id):
    reviews_data = load_reviews("data/reviews.json")
    review = find_review_by_id(reviews_data, review_id)

    context = {
        "review": review,
    }
    return render(request, "reviews/review_detail.html", context, status=404 if review is None else 200)