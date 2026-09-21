from typing import List, Dict, Optional


def add_podcast(podcasts: List[Dict], title: str) -> bool:
    for p in podcasts:
        if p["title"].lower() == title.lower():
            print(f"Ошибка: подкаст с названием '{title}' уже существует!")
            return False
    # Генерация нового ID (максимальный существующий + 1)
    new_id = max((p["id"] for p in podcasts), default=0) + 1
    podcasts.append({"id": new_id, "title": title})
    print(f"Подкаст '{title}' успешно добавлен (ID: {new_id}).")
    return True


def find_podcast_by_id(podcasts: List[Dict],
                       podcast_id: int) -> Optional[Dict]:
    for p in podcasts:
        if p["id"] == podcast_id:
            return p
    return None


def get_all_podcasts(podcasts: List[Dict]) -> List[Dict]:
    return podcasts
