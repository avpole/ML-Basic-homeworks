# homework_04/model/storage/base_storage.py
from abc import ABC, abstractmethod
from typing import Optional
from media.base_media_file import BaseMediaFile
from media.file_registry import create_file_from_metadata

class BaseStorage(ABC):
    """Абстрактное хранилище файлов"""

    @abstractmethod
    def save(self, file: BaseMediaFile):
        pass

    @abstractmethod
    def delete(self, file: BaseMediaFile):
        pass

    @abstractmethod
    def fetch_file_and_metadata(self, file_id: str) -> dict:
        """Получает файл и его метаданные из хранилища """
        pass

    def load(self, file_id: str) -> Optional[BaseMediaFile]:
        """Создает объект нужного типа через фабрику"""
        try:
            metadata = self.fetch_file_and_metadata(file_id)
            return create_file_from_metadata(metadata)
        except Exception:
            return None