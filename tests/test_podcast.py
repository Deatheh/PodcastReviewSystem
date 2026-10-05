import os
import sys

# Добавляем корень проекта в путь поиска модулей
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from podcasts import Podcast
from podcast_manager import PodcastManager


def test_podcast_creation():
    podcast = Podcast(1, "Test Podcast", 1)
    assert podcast.podcast_id == 1
    assert podcast.title == "Test Podcast"
    assert podcast.author_id == 1


def test_podcast_to_dict_and_from_data():
    podcast = Podcast(1, "Test Podcast", 1)
    data = podcast.to_dict()
    restored = Podcast.from_data(data)
    assert restored.title == "Test Podcast"
    assert restored.author_id == 1


def test_podcast_matches_title():
    podcast = Podcast(1, "Python Podcast", 1)
    assert podcast.matches_title("python") is True
    assert podcast.matches_title("java") is False


def test_podcast_str():
    podcast = Podcast(1, "Test Podcast")
    assert "Test Podcast" in str(podcast)


def test_add_podcast():
    manager = PodcastManager()
    podcast = manager.add_podcast("Test Podcast", 1)
    assert podcast is not None
    assert len(manager.get_all()) == 1


def test_add_duplicate_podcast():
    manager = PodcastManager()
    manager.add_podcast("Test Podcast", 1)
    assert manager.add_podcast("Test Podcast", 2) is None


def test_add_short_title():
    manager = PodcastManager()
    assert manager.add_podcast("abc", 1) is None


def test_find_by_id():
    manager = PodcastManager()
    podcast = manager.add_podcast("Test Podcast", 1)
    assert manager.find_by_id(podcast.podcast_id) is not None
    assert manager.find_by_id(999) is None


def test_find_by_title():
    manager = PodcastManager()
    manager.add_podcast("Python Podcast", 1)
    manager.add_podcast("Java Podcast", 1)
    found = manager.find_by_title("python")
    assert len(found) == 1
    assert found[0].title == "Python Podcast"


if __name__ == "__main__":
    # Простой самодельный раннер — запускает все функции test_*
    import traceback

    tests = [
        (name, obj)
        for name, obj in list(globals().items())
        if name.startswith("test_") and callable(obj)
    ]
    passed = 0
    failed = 0
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