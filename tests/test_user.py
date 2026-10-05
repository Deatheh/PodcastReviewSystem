import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from user import User
from user_manager import UserManager


def test_user_creation():
    user = User(1, "testuser", "test@example.com")
    assert user.user_id == 1
    assert user.username == "testuser"
    assert user.email == "test@example.com"


def test_user_to_dict_and_from_data():
    user = User(1, "testuser", "test@example.com")
    data = user.to_dict()
    restored = User.from_data(data)
    assert restored.username == "testuser"


def test_user_str():
    user = User(1, "testuser", "test@example.com")
    assert "testuser" in str(user)


def test_add_user():
    manager = UserManager()
    user = manager.add_user("testuser", "test@example.com")
    assert user is not None
    assert len(manager.get_all()) == 1


def test_add_duplicate_user():
    manager = UserManager()
    manager.add_user("testuser", "test@example.com")
    assert manager.add_user("testuser", "test2@example.com") is None


def test_login_success():
    manager = UserManager()
    manager.add_user("testuser", "test@example.com")
    assert manager.login("testuser") is True
    assert manager.get_current_user() is not None


def test_login_failure():
    manager = UserManager()
    assert manager.login("nonexistent") is False


def test_find_by_id():
    manager = UserManager()
    user = manager.add_user("testuser", "test@example.com")
    assert manager.find_by_id(user.user_id) is user
    assert manager.find_by_id(999) is None


if __name__ == "__main__":
    import traceback

    tests = [
        (name, obj)
        for name, obj in list(globals().items())
        if name.startswith("test_") and callable(obj)
    ]
    passed = failed = 0
    for name, func in tests:
        try:
            func()
            print(f"[OK]   {name}")
            passed += 1
        except Exception:
            print(f"[FAIL] {name}")
            traceback.print_exc()
            failed += 1
    print(f"\nИтого: {passed} прошло, {failed} упало")
    sys.exit(1 if failed else 0)