# homework_04/model/media/base_media_file.py
from abc import ABC
from datetime import datetime


class BaseMediaFile(ABC):
    """Базовый класс для любого медиа-файла"""

    def __init__(self, name: str, size: int, owner: str, format: str, created_at: datetime | None = None):
        self.name = name
        self.size = size
        self.owner = owner
        self.format = format
        self.created_at = created_at or datetime.now()

    def get_metadata(self) -> dict:
        """Вернуть словарь с метаданными"""
        return {
            "type": self.type,
            "name": self.name,
            "size": self.size,
            "owner": self.owner,
            "format": self.format,
        }
    
    @property
    def type(self) -> str:
        """Тип файла = имя класса в нижнем регистре"""
        return self.__class__.__name__.replace("File", "").lower()

    def rename(self, new_name: str):
        """Переименовать файл"""
        self.name = new_name

    def delete(self):
        """Удалить файл (реализация будет зависеть от хранилища)"""
        pass

    def save(self):
        """Сохранить файл в хранилище"""
        pass

    def convert_format(self, target_format: str):
        """Конвертировать в другой формат (mp3 → wav, etc.)"""
        print(f"Конвертация {self.name} в {target_format}")
