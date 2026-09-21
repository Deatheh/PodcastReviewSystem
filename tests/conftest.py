import sys
import os

# Добавляем корневую директорию проекта в пути поиска модулей
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')
))
