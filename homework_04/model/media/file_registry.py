# homework_04/model/media/file_registry.py
from typing import Type
from .base_media_file import BaseMediaFile

_file_registry: dict[str, Type[BaseMediaFile]] = {}

def register_file_type(file_class: Type[BaseMediaFile]):
    """Регистрируем класс файла в реестре"""
    key = file_class.__name__.lower()
    _file_registry[key] = file_class

def create_file_from_metadata(data: dict) -> BaseMediaFile:
    """Создаем объект нужного класса по метаданным"""
    file_type = data.get("type")
    if file_type:
        cls = _file_registry.get(file_type)
        if cls is None:
            raise ValueError(f"Неизвестный тип файла: {file_type}")
        return cls(**data)
    else:
        raise ValueError(f"Тип файла не задан в data = {data}")
