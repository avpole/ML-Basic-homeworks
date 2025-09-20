# homework_04/model/media/base_audio_video_stream_file.py
from .base_media_file import BaseMediaFile

class BaseAudioVideoStreamFile(BaseMediaFile):
    """Аудиофайл"""

    def __init__(self, name: str, size: int, owner: str,
                 format: str, codec_type: str, bitrate: int, duration: float, **kwargs):
        super().__init__(name, size, owner, format, **kwargs)
        self.codec_type = codec_type
        self.bitrate = bitrate
        self.duration = duration

    def get_metadata(self) -> dict:
        """Вернуть словарь с метаданными"""
        base_meta = super().get_metadata()
        return base_meta | {
            "codec_type": self.codec_type,
            "bitrate": self.bitrate,
            "duration": self.duration
        }
    
    def get_stream(self):
        """Получить поток для обработки/воспроизведения"""
        pass