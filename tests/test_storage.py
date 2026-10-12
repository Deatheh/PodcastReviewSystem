import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from storage import StorageManager


def _make_storage():
    test_dir = "test_data"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    return StorageManager(test_dir), test_dir


def test_save_and_load_json():
    storage, test_dir = _make_storage()
    try:
        data = [{"id": 1, "name": "Test"}, {"id": 2, "name": "Test2"}]
        assert storage.save_json("test.json", data) is True
        loaded = storage.load_json("test.json")
        assert len(loaded) == 2
        assert loaded[0]["name"] == "Test"
    finally:
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)


def test_load_nonexistent_file():
    storage, test_dir = _make_storage()
    try:
        assert storage.load_json("nonexistent.json") == []
    finally:
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)


def test_save_and_load_users():
    storage, test_dir = _make_storage()
    try:
        users = [{"user_id": 1, "username": "admin", "email": "a@b.com"}]
        assert storage.save_users(users) is True
        assert len(storage.load_users()) == 1
    finally:
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)


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