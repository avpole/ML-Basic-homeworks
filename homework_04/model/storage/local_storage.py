# homework_04/model/storage/local_storage.py
from typing import Optional
from .base_storage import BaseStorage
from media.base_media_file import BaseMediaFile


class LocalStorage(BaseStorage):
    """Локальное хранилище"""

    def save(self, file: BaseMediaFile):
        print(f"Сохраняем {file.name} на локальном диске")

    def delete(self, file: BaseMediaFile):
        print(f"Удаляем {file.name} с локального диска")

    def fetch_file_and_metadata(self, file_id: str) -> dict:
        # Пример получения аудио файла с локального диска
        return {}
