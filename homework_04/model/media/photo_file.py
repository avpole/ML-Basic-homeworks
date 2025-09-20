# homework_04/model/media/photo_file.py
from typing import Optional
from .base_media_file import BaseMediaFile

class PhotoFile(BaseMediaFile):
    """Фотография"""

    def __init__(self, name: str, size: int, owner: str, format: str,
                 resolution: str, camera_model: str, **kwargs):
        super().__init__(name, size, owner, format, **kwargs)
        self.resolution = resolution
        self.camera_model = camera_model

    def get_metadata(self) -> dict:
        base_meta = super().get_metadata()
        return base_meta | {

            "resolution": self.resolution,
            "camera_model": self.camera_model
        }

    def resize(self, new_resolution: str) -> 'PhotoFile':
        """Изменить размер изображения, возвращает новый объект"""
        print(f"Изменение разрешения {self.name} на {new_resolution}")
        return PhotoFile(
            name=f"{self.name}_resized",
            size=self.size,  # при реальной реализации можно пересчитать размер
            owner=self.owner,
            format=self.format,
            resolution=new_resolution,
            camera_model=self.camera_model
        )


    def crop(self, x1: int, y1: int, x2: int, y2: int) ->  Optional['PhotoFile']:
        """Вырезать фрагмент по координатам (x1, y1) – (x2, y2)"""
        print(f"Вырезка фрагмента из {self.name} по координатам ({x1}, {y1})–({x2}, {y2})")
        width = x2 - x1
        height = y2 - y1
        new_resolution = f"{width}x{height}"
        return PhotoFile(
            name=f"{self.name}_cropped",
            size=self.size,  # при реальной реализации размер может измениться
            owner=self.owner,
            format=self.format,
            resolution=new_resolution,
            camera_model=self.camera_model
        )
