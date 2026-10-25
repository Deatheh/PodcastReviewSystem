import json
from db.database import get_connection

USERS_FILE = "data/users.json"
PODCASTS_FILE = "data/podcasts.json"
REVIEWS_FILE = "data/reviews.json"


def load_json(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def import_users(conn):
    users = load_json(USERS_FILE)
    conn.executemany(
        "INSERT INTO users (id, username, email) VALUES (?, ?, ?)",
        [(u["user_id"], u["username"], u["email"]) for u in users],
    )


def import_podcasts(conn):
    podcasts = load_json(PODCASTS_FILE)
    conn.executemany(
        "INSERT INTO podcasts (id, title, author_id) VALUES (?, ?, ?)",
        [
            (p["podcast_id"], p["title"], p.get("author_id"))
            for p in podcasts
        ],
    )


def import_reviews(conn):
    reviews = load_json(REVIEWS_FILE)
    conn.executemany(
        "INSERT INTO reviews (id, podcast_id, user_id, text, rating) "
        "VALUES (?, ?, ?, ?, ?)",
        [
            (
                r["review_id"],
                r["podcast_id"],
                r["user_id"],
                r["text"],
                r.get("rating"),
            )
            for r in reviews
        ],
    )


def main():
    conn = get_connection()
    try:
        import_users(conn)
        import_podcasts(conn)
        import_reviews(conn)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()