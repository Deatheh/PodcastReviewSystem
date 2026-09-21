from reviews import add_review, get_reviews_for_podcast


def test_add_review_success():
    podcasts = [{"id": 1, "title": "Test Podcast"}]
    reviews = []
    result = add_review(reviews, podcasts, 1, "Great show!")
    assert result is True
    assert len(reviews) == 1
    assert reviews[0]["text"] == "Great show!"


def test_add_review_to_nonexistent_podcast():
    podcasts = []
    reviews = []
    result = add_review(reviews, podcasts, 99, "Bad show!")
    assert result is False
    assert len(reviews) == 0


def test_get_reviews_for_podcast_lambda():
    reviews = [
        {"id": 1, "podcast_id": 1, "text": "Good"},
        {"id": 2, "podcast_id": 2, "text": "Bad"},
        {"id": 3, "podcast_id": 1, "text": "Excellent"}
    ]
    filtered = get_reviews_for_podcast(reviews, 1)
    assert len(filtered) == 2
    assert all(r["podcast_id"] == 1 for r in filtered)
