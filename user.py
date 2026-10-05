"""Модель пользователя."""
from typing import Dict, Any


class User:
    """Пользователь системы."""

    def __init__(self, user_id: int, username: str, email: str) -> None:
        self.user_id: int = user_id
        self.username: str = username
        self.email: str = email

    @classmethod
    def from_data(cls, data: Dict[str, Any]) -> "User":
        """Создать объект User из словаря."""
        return cls(
            user_id=data["user_id"],
            username=data["username"],
            email=data["email"],
        )

    def to_dict(self) -> Dict[str, Any]:
        """Преобразовать объект в словарь для JSON."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
        }

    def __str__(self) -> str:
        return f"User(id={self.user_id}, username='{self.username}', email='{self.email}')"

    def __repr__(self) -> str:
        return self.__str__()