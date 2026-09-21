from podcasts import add_podcast, get_all_podcasts, find_podcast_by_id
from reviews import add_review, get_reviews_for_podcast
from storage import load_podcasts, save_podcasts, load_reviews, save_reviews
from utils import input_int, input_non_empty_string

PODCASTS_FILE = "data/podcasts.json"
REVIEWS_FILE = "data/reviews.json"


def show_menu() -> None:
    print("\n=== Система отзывов о подкастах ===")
    print("1. Добавить подкаст")
    print("2. Показать все подкасты")
    print("3. Добавить отзыв к подкасту")
    print("4. Показать отзывы о подкасте")
    print("0. Выход")


def main() -> None:
    # Загрузка данных при старте
    podcasts = load_podcasts(PODCASTS_FILE)
    reviews = load_reviews(REVIEWS_FILE)

    # Демонстрация преемственности ПР1
    if not podcasts:
        add_podcast(podcasts, "Podcast 1")
        add_podcast(podcasts, "Podcast 2")
        add_review(reviews, podcasts, 1, "comment 1 to 1 podcast")

    while True:
        show_menu()
        choice = input_int("Выберите действие: ")

        if choice == 1:
            title = input_non_empty_string("Введите название подкаста (мин. 4 симв.): ")
            add_podcast(podcasts, title)
            save_podcasts(PODCASTS_FILE, podcasts)

        elif choice == 2:
            all_podcasts = get_all_podcasts(podcasts)
            if not all_podcasts:
                print("Список подкастов пуст.")
            else:
                print("\nСписок подкастов:")
                for p in all_podcasts:
                    print(f"ID: {p['id']}, Название: {p['title']}")

        elif choice == 3:
            podcast_id = input_int("Введите ID подкаста: ")
            if find_podcast_by_id(podcasts, podcast_id):
                text = input_non_empty_string("Введите текст отзыва: ", min_length=1)
                add_review(reviews, podcasts, podcast_id, text)
                save_reviews(REVIEWS_FILE, reviews)
            else:
                print(f"Ошибка: подкаст с ID {podcast_id} не существует.")

        elif choice == 4:
            podcast_id = input_int("Введите ID подкаста для просмотра отзывов: ")
            podcast = find_podcast_by_id(podcasts, podcast_id)
            if podcast:
                pod_reviews = get_reviews_for_podcast(reviews, podcast_id)
                print(f"\nОтзывы о подкасте '{podcast['title']}':")
                if not pod_reviews:
                    print("Отзывов пока нет.")
                for r in pod_reviews:
                    print(f"- {r['text']}")
            else:
                print(f"Ошибка: подкаст с ID {podcast_id} не найден.")

        elif choice == 0:
            print("Выход из программы. Данные сохранены.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
