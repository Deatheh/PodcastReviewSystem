import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reviews import Review
from review_manager import ReviewManager
from podcast_manager import PodcastManager


def setup_managers():
    pm = PodcastManager()
    rm = ReviewManager()
    podcast = pm.add_podcast("Test Podcast", 1)
    return pm, rm, podcast


def test_review_creation():
    review = Review(1, 1, 1, "Great podcast!")
    assert review.review_id == 1
    assert review.text == "Great podcast!"


def test_review_to_dict_and_from_data():
    review = Review(1, 1, 1, "Great podcast!")
    data = review.to_dict()
    restored = Review.from_data(data)
    assert restored.text == "Great podcast!"


def test_review_str():
    review = Review(1, 1, 1, "Great!")
    assert "Great!" in str(review)


def test_add_review_success():
    pm, rm, podcast = setup_managers()
    result = rm.add_review(podcast.podcast_id, 1, "Great!", pm)
    assert result is True
    assert len(rm.get_all()) == 1


def test_add_review_nonexistent_podcast():
    pm, rm, _ = setup_managers()
    assert rm.add_review(999, 1, "Great!", pm) is False


def test_add_empty_review():
    pm, rm, podcast = setup_managers()
    assert rm.add_review(podcast.podcast_id, 1, "   ", pm) is False


def test_get_reviews_for_podcast():
    pm, rm, podcast = setup_managers()
    rm.add_review(podcast.podcast_id, 1, "Review 1", pm)
    rm.add_review(podcast.podcast_id, 2, "Review 2", pm)
    assert len(rm.get_for_podcast(podcast.podcast_id)) == 2


def test_get_reviews_for_user():
    pm, rm, podcast = setup_managers()
    rm.add_review(podcast.podcast_id, 1, "Review 1", pm)
    rm.add_review(podcast.podcast_id, 2, "Review 2", pm)
    assert len(rm.get_for_user(1)) == 1


if __name__ == "__main__":
    import traceback

    tests = [
        (name, obj)
        for name, obj in list(globals().items())
        if name.startswith("test_") and callable(obj)
    ]
    passed = failed = 0
    for name, func in tests:
        try:
            func()
            print(f"[OK]   {name}")
            passed += 1
        except Exception:
            print(f"[FAIL] {name}")
            traceback.print_exc()
            failed += 1
    print(f"\nИтого: {passed} прошло, {failed} упало")
    sys.exit(1 if failed else 0)