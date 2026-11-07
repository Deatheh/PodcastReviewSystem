"""
Переносит данные из исходной базы data/podcast_system.sqlite
в целевую базу Django (db.sqlite3) через ORM.
Запускать после применения миграций:
    python manage.py migrate
    python db/import_sqlite_to_orm.py
"""

import os
import sqlite3
import sys
from pathlib import Path

import django
from django.db import transaction

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "podcast_system.settings")
django.setup()

from podcasts.models import Podcast          # noqa: E402
from reviews.models import Review            # noqa: E402
from users.models import User                # noqa: E402

SOURCE_DB = BASE_DIR / "data" / "podcast_system.sqlite"


def main():
    if not SOURCE_DB.exists():
        raise FileNotFoundError(f"Исходная база не найдена: {SOURCE_DB}")

    with sqlite3.connect(SOURCE_DB) as connection:
        connection.row_factory = sqlite3.Row

        users = connection.execute(
            "SELECT id, username, email FROM users ORDER BY id"
        ).fetchall()
        podcasts = connection.execute(
            "SELECT id, title, author_id FROM podcasts ORDER BY id"
        ).fetchall()
        reviews = connection.execute(
            "SELECT id, podcast_id, user_id, text, rating FROM reviews ORDER BY id"
        ).fetchall()

    with transaction.atomic():
        for row in users:
            User.objects.update_or_create(
                pk=row["id"],
                defaults={
                    "username": row["username"],
                    "email": row["email"],
                },
            )

        for row in podcasts:
            Podcast.objects.update_or_create(
                pk=row["id"],
                defaults={
                    "title": row["title"],
                    "author_id": row["author_id"],   # None допустим
                },
            )

        for row in reviews:
            Review.objects.update_or_create(
                pk=row["id"],
                defaults={
                    "podcast_id": row["podcast_id"],
                    "user_id": row["user_id"],
                    "text": row["text"] or "",       # NULL -> ""
                    "rating": row["rating"] or None, # "" -> None; числа сохраняются
                },
            )

    print("Перенос завершён.")
    print(f"Пользователей: {User.objects.count()}")
    print(f"Подкастов: {Podcast.objects.count()}")
    print(f"Отзывов: {Review.objects.count()}")


if __name__ == "__main__":
    main()