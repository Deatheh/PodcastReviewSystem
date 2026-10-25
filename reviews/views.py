import sqlite3
from django.shortcuts import render

DB_PATH = "data/podcast_system.sqlite"


def reviews_list(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    reviews = conn.execute(
        "SELECT r.id, r.text, r.rating, p.title AS podcast_title, u.username "
        "FROM reviews r "
        "JOIN podcasts p ON r.podcast_id = p.id "
        "JOIN users u ON r.user_id = u.id "
        "ORDER BY r.id;"
    ).fetchall()
    conn.close()
    return render(request, "reviews/review_list.html", {"reviews": reviews})


def review_detail(request, review_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    review = conn.execute(
        "SELECT r.id, r.text, r.rating, p.title AS podcast_title, u.username "
        "FROM reviews r "
        "JOIN podcasts p ON r.podcast_id = p.id "
        "JOIN users u ON r.user_id = u.id "
        "WHERE r.id = ?;",
        (review_id,),
    ).fetchone()
    conn.close()

    if review is None:
        from homepage.views import page_not_found
        return page_not_found(request, exception=None)

    return render(request, "reviews/review_detail.html", {"review": review})


def statistics(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    stats = conn.execute(
        "SELECT p.title AS podcast_title, COUNT(r.id) AS reviews_count, AVG(r.rating) AS avg_rating "
        "FROM podcasts p "
        "LEFT JOIN reviews r ON p.id = r.podcast_id "
        "GROUP BY p.id, p.title "
        "ORDER BY reviews_count DESC;"
    ).fetchall()
    conn.close()
    return render(request, "reviews/statistics.html", {"stats": stats})