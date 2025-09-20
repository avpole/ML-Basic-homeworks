# homework_04/storage/ftp_storage.py
from typing import Optional
from .base_remote_storage import BaseRemoteStorage
from media.base_media_file import BaseMediaFile


class FtpStorage(BaseRemoteStorage):
    """Хранилище файлов через FTP"""

    def __init__(self, host: str, port: int, user_name: str, password: str):
        super().__init__(host, user_name, password, False)
        self.port = port

        try:
            self.connect()
        except Exception:
            pass

    def connect(self):
        """Установить соединение с FTP-сервером"""
        print(f"Подключаемся к FTP {self.host}:{self.port} как {self.user_name}")

    def disconnect(self):
        """Разрываем соединение с FTP-сервером"""
        print(f"Отключаемся от FTP {self.host}:{self.port} как {self.user_name}")

    def save(self, file: BaseMediaFile):
        """Сохранить файл на FTP-сервере"""
        print(f"Сохраняем {file.name} на FTP сервере")

    def delete(self, file: BaseMediaFile):
        """Удалить файл с FTP-сервера"""
        print(f"Удаляем {file.name} с FTP сервера")

    def fetch_file_and_metadata(self, file_id: str) -> dict:
        # Пример получения видео файла из FTP
        return {
            "type": "videofile",
            "name": file_id,
            "size": 500000,
            "owner": "Vasy",
            "format": "mp4",
            "resolution": "1920x1080",
            "codec_type": "H.264",
            "bitrate": 4000,
            "duration": 7200
        }