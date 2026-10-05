"""Менеджер пользователей."""
from typing import List, Optional, Dict, Any
from user import User


class UserManager:
    """Управляет коллекцией пользователей и текущей сессией."""

    def __init__(self) -> None:
        self.users: List[User] = []
        self.current_user: Optional[User] = None

    def add_user(self, username: str, email: str) -> Optional[User]:
        """Зарегистрировать нового пользователя."""
        clean_username = username.strip()
        clean_email = email.strip()

        if any(u.username.lower() == clean_username.lower() for u in self.users):
            print(f"Ошибка: пользователь '{clean_username}' уже существует!")
            return None
        if "@" not in clean_email or "." not in clean_email:
            print("Ошибка: некорректный формат email!")
            return None

        new_id = max((u.user_id for u in self.users), default=0) + 1
        new_user = User(new_id, clean_username, clean_email)
        self.users.append(new_user)
        print(f"Пользователь '{clean_username}' успешно зарегистрирован (ID: {new_id})")
        return new_user

    def login(self, username: str) -> bool:
        """Войти в систему по имени пользователя."""
        user = next(
            (u for u in self.users if u.username.lower() == username.strip().lower()),
            None,
        )
        if user:
            self.current_user = user
            print(f"Добро пожаловать, {user.username}!")
            return True
        print(f"Ошибка: пользователь '{username}' не найден!")
        return False

    def logout(self) -> None:
        """Выйти из системы."""
        if self.current_user:
            print(f"До свидания, {self.current_user.username}!")
            self.current_user = None

    def get_current_user(self) -> Optional[User]:
        """Вернуть текущего пользователя или None."""
        return self.current_user

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Найти пользователя по идентификатору."""
        return next((u for u in self.users if u.user_id == user_id), None)

    def get_all(self) -> List[User]:
        """Вернуть копию списка пользователей."""
        return self.users.copy()

    def load_from_list(self, users_data: List[Dict[str, Any]]) -> None:
        """Загрузить пользователей из списка словарей."""
        self.users = [User.from_data(data) for data in users_data]

    def save_to_list(self) -> List[Dict[str, Any]]:
        """Сериализовать пользователей в список словарей."""
        return [user.to_dict() for user in self.users]