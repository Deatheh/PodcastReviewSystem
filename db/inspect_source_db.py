import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE_DB = BASE_DIR / "data" / "podcast_system.sqlite"

with sqlite3.connect(SOURCE_DB) as conn:
    conn.row_factory = sqlite3.Row

    print("=== Структура таблицы reviews ===")
    for col in conn.execute("PRAGMA table_info(reviews)").fetchall():
        print(f"  name={col['name']!r}, type={col['type']!r}, "
              f"notnull={col['notnull']}, pk={col['pk']}, default={col['dflt_value']!r}")

    total = conn.execute("SELECT COUNT(*) FROM reviews").fetchone()[0]
    print(f"\nВсего записей: {total}")

    for col in ("text", "rating", "podcast_id", "user_id"):
        try:
            n = conn.execute(
                f"SELECT COUNT(*) FROM reviews WHERE {col} IS NULL"
            ).fetchone()[0]
            print(f"  NULL в {col}: {n}")
        except sqlite3.OperationalError as e:
            print(f"  Столбец {col}: {e}")

    print("\n=== Первые 10 записей reviews ===")
    for row in conn.execute("SELECT * FROM reviews LIMIT 10").fetchall():
        print(dict(row))