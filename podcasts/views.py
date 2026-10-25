import sqlite3
from django.shortcuts import render

DB_PATH = "data/podcast_system.sqlite"


def podcasts_list(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    podcasts = conn.execute("SELECT id, title FROM podcasts ORDER BY title;").fetchall()
    conn.close()
    return render(request, "podcasts/podcast_list.html", {"podcasts": podcasts})


def podcast_detail(request, podcast_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    podcast = conn.execute(
        "SELECT id, title, author_id FROM podcasts WHERE id = ?;",
        (podcast_id,),
    ).fetchone()

    if podcast is None:
        conn.close()
        # Вызываем вашу функцию 404 из homepage
        from homepage.views import page_not_found
        return page_not_found(request, exception=None)

    reviews = conn.execute(
        "SELECT r.id, r.text, r.rating, u.username "
        "FROM reviews r JOIN users u ON r.user_id = u.id "
        "WHERE r.podcast_id = ?;",
        (podcast_id,),
    ).fetchall()
    conn.close()
    return render(request, "podcasts/podcast_detail.html", {"podcast": podcast, "reviews": reviews})


def podcasts_search(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        results = conn.execute(
            "SELECT id, title FROM podcasts WHERE title LIKE ?;",
            (f"%{query}%",),
        ).fetchall()
        conn.close()
    return render(request, "podcasts/search.html", {"query": query, "results": results})