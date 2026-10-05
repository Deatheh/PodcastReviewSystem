"""Точка входа в приложение."""
from storage import StorageManager
from user_manager import UserManager
from podcast_manager import PodcastManager
from review_manager import ReviewManager
from utils import input_int, input_non_empty_string, input_email


class PodcastReviewSystem:
    """Консольное приложение «Система отзывов о подкастах»."""

    def __init__(self) -> None:
        self.storage = StorageManager()
        self.user_manager = UserManager()
        self.podcast_manager = PodcastManager()
        self.review_manager = ReviewManager()
        self._load_data()

    def _load_data(self) -> None:
        """Загрузить данные из JSON в объектную модель."""
        self.user_manager.load_from_list(self.storage.load_users())
        self.podcast_manager.load_from_list(self.storage.load_podcasts())
        self.review_manager.load_from_list(self.storage.load_reviews())
        print(
            f"Загружено: {len(self.user_manager.get_all())} пользователей, "
            f"{len(self.podcast_manager.get_all())} подкастов, "
            f"{len(self.review_manager.get_all())} отзывов"
        )

    def _save_data(self) -> None:
        """Сохранить объектную модель в JSON."""
        self.storage.save_users(self.user_manager.save_to_list())
        self.storage.save_podcasts(self.podcast_manager.save_to_list())
        self.storage.save_reviews(self.review_manager.save_to_list())

    def _show_main_menu(self) -> None:
        """Показать главное меню."""
        print("\n=== Система отзывов о подкастах ===")
        user = self.user_manager.get_current_user()
        if user:
            print(f"Вы вошли как: {user.username} ({user.email})")
        print("1. Регистрация / Вход")
        if user:
            print("2. Добавить подкаст")
            print("3. Показать все подкасты")
            print("4. Найти подкаст по названию")
            print("5. Добавить отзыв")
            print("6. Показать отзывы о подкасте")
            print("7. Мои отзывы")
            print("8. Выйти из аккаунта")
        print("0. Выход из программы")

    def _auth_menu(self) -> None:
        """Подменю аутентификации."""
        print("\n=== Аутентификация ===")
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("0. Назад")
        choice = input_int("Выберите действие: ")
        if choice == 1:
            username = input("Введите имя пользователя: ").strip()
            self.user_manager.login(username)
        elif choice == 2:
            username = input_non_empty_string(
                "Введите имя пользователя (мин. 4 симв.): ", min_length=4
            )
            email = input_email("Введите email: ")
            self.user_manager.add_user(username, email)

    def _handle_add_podcast(self, author_id: int) -> None:
        title = input_non_empty_string(
            "Введите название подкаста (мин. 4 симв.): ", min_length=4
        )
        if self.podcast_manager.add_podcast(title, author_id):
            self._save_data()

    def _handle_show_podcasts(self) -> None:
        podcasts = self.podcast_manager.get_all()
        if not podcasts:
            print("\nСписок подкастов пуст")
            return
        print("\n=== Список подкастов ===")
        for p in podcasts:
            print(f"ID: {p.podcast_id}, Название: {p.title}")

    def _handle_find_podcast(self) -> None:
        query = input_non_empty_string("Введите часть названия: ")
        found = self.podcast_manager.find_by_title(query)
        if not found:
            print("Подкасты не найдены")
            return
        print("\n=== Результаты поиска ===")
        for p in found:
            print(f"ID: {p.podcast_id}, Название: {p.title}")

    def _handle_add_review(self, user_id: int) -> None:
        podcast_id = input_int("Введите ID подкаста: ")
        if not self.podcast_manager.find_by_id(podcast_id):
            print(f"Ошибка: подкаст с ID {podcast_id} не найден")
            return
        text = input_non_empty_string("Введите текст отзыва: ", min_length=1)
        if self.review_manager.add_review(
            podcast_id, user_id, text, self.podcast_manager
        ):
            self._save_data()

    def _handle_show_reviews(self) -> None:
        podcast_id = input_int("Введите ID подкаста: ")
        podcast = self.podcast_manager.find_by_id(podcast_id)
        if not podcast:
            print(f"Ошибка: подкаст с ID {podcast_id} не найден")
            return
        reviews = self.review_manager.get_for_podcast(podcast_id)
        print(f"\n=== Отзывы о подкасте '{podcast.title}' ===")
        if not reviews:
            print("Отзывов пока нет")
            return
        for r in reviews:
            user = self.user_manager.find_by_id(r.user_id)
            name = user.username if user else "Unknown"
            print(f"[{name}]: {r.text}")

    def _handle_my_reviews(self, user_id: int) -> None:
        reviews = self.review_manager.get_for_user(user_id)
        print("\n=== Ваши отзывы ===")
        if not reviews:
            print("Вы пока не оставляли отзывов")
            return
        for r in reviews:
            podcast = self.podcast_manager.find_by_id(r.podcast_id)
            title = podcast.title if podcast else "Unknown"
            print(f"Подкаст '{title}': {r.text}")

    def run(self) -> None:
        """Главный цикл приложения."""
        if not self.user_manager.get_all():
            self.user_manager.add_user("admin", "admin@example.com")
        if not self.podcast_manager.get_all():
            self.podcast_manager.add_podcast("Python Podcast", 1)

        while True:
            self._show_main_menu()
            choice = input_int("Выберите действие: ")
            current_user = self.user_manager.get_current_user()

            if choice == 1:
                self._auth_menu()
                self._save_data()
            elif choice == 2 and current_user:
                self._handle_add_podcast(current_user.user_id)
            elif choice == 3 and current_user:
                self._handle_show_podcasts()
            elif choice == 4 and current_user:
                self._handle_find_podcast()
            elif choice == 5 and current_user:
                self._handle_add_review(current_user.user_id)
            elif choice == 6 and current_user:
                self._handle_show_reviews()
            elif choice == 7 and current_user:
                self._handle_my_reviews(current_user.user_id)
            elif choice == 8 and current_user:
                self.user_manager.logout()
            elif choice == 0:
                self._save_data()
                print("Выход из программы. До свидания!")
                break
            else:
                if not current_user and choice not in (0, 1):
                    print("Сначала войдите в систему!")
                else:
                    print("Неверный выбор, попробуйте снова")


def main() -> None:
    """Точка запуска приложения."""
    app = PodcastReviewSystem()
    app.run()


if __name__ == "__main__":
    main()