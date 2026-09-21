from typing import List, Dict
from podcasts import find_podcast_by_id


def add_review(reviews: List[Dict], podcasts: List[Dict],
               podcast_id: int, text: str) -> bool:
    podcast = find_podcast_by_id(podcasts, podcast_id)
    if not podcast:
        print(f"Ошибка: подкаст с ID {podcast_id} не найден.")
        return False
    new_id = max((r["id"] for r in reviews), default=0) + 1
    reviews.append({
        "id": new_id,
        "podcast_id": podcast_id,
        "text": text
    })
    print(f"Отзыв успешно добавлен к подкасту '{podcast['title']}'.")
    return True


def get_reviews_for_podcast(reviews: List[Dict],
                            podcast_id: int) -> List[Dict]:
    return list(filter(lambda r: r["podcast_id"] == podcast_id, reviews))
