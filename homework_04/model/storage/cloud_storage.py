# homework_04/model/storage/ftp_storage.py
from typing import Optional
from .base_remote_storage import BaseRemoteStorage
from media.base_media_file import BaseMediaFile

class CloudStorage(BaseRemoteStorage):
    """Локальное хранилище"""

    def __init__(self, host: str, user_name: str, password: str):
        self.host = host
        self.user_name = user_name
        self.password = password


    def connect(self):
        """Установить соединение с облаком"""
        print(f"Подключаемся к {self.host} как {self.user_name}")

    def disconnect(self):
        """Разрываем соединение с облаком"""
        print(f"Отключаемся от {self.host} как {self.user_name}")

    def save(self, file: BaseMediaFile):
        print(f"Сохраняем {file.name} в облако {self.host}")

    def delete(self, file: BaseMediaFile):
        print(f"Удаляем {file.name} из облака {self.host}")

    def fetch_file_and_metadata(self, file_id: str) -> dict:
        # пример получаем файл, получаем его метаданные и через фабрику возвращаем нужный экземпляр класса
        return {
            "type": "photofile",  # здесь динамически определяется
            "name": file_id,
            "size": 2048,
            "owner": "Goga",
            "format": "jpg",
            "resolution": "4000x3000",
            "camera_model": "Canon EOS 5D"
        }