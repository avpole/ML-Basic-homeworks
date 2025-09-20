# homework_04/model/media/video_file.py
from typing import Optional
from .photo_file import PhotoFile
from .base_audio_video_stream_file import BaseAudioVideoStreamFile


class VideoFile(BaseAudioVideoStreamFile):
    """Видеофайл"""

    def __init__(self, name: str, size: int, owner: str,
                 format: str, codec_type: str, bitrate: int, duration: float,
                 resolution: str, **kwargs):
        super().__init__(name, size, owner, format, codec_type, bitrate, duration, **kwargs)
        self.resolution = resolution

    def get_metadata(self) -> dict:
        base_meta = super().get_metadata()
        return base_meta | {
            "resolution": self.resolution
        }

    def extract_frame(self, timestamp: float) -> PhotoFile:
        """Извлечь кадр на заданной секунде"""
        print(f"Извлечение кадра из {self.name} на {timestamp} сек.")
        return PhotoFile(
            name=f"{self.name}_frame_{int(timestamp)}",
            size=1024,  # примерное значение
            owner=self.owner,
            format="jpg",
            resolution=self.resolution,
            camera_model="frame_capture"
        )