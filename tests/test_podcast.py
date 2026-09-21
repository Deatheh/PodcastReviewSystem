from podcasts import add_podcast, find_podcast_by_id


def test_add_podcast_success():
    podcasts = []
    result = add_podcast(podcasts, "Test Podcast")
    assert result is True
    assert len(podcasts) == 1
    assert podcasts[0]["title"] == "Test Podcast"


def test_add_podcast_duplicate():
    podcasts = [{"id": 1, "title": "Test Podcast"}]
    result = add_podcast(podcasts, "Test Podcast")
    assert result is False
    assert len(podcasts) == 1


def test_find_podcast_by_id():
    podcasts = [{"id": 1, "title": "Test Podcast"}]
    assert find_podcast_by_id(podcasts, 1) is not None
    assert find_podcast_by_id(podcasts, 99) is None
