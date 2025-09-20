# homework_04/model/media/audio_file.py
from .base_audio_video_stream_file import BaseAudioVideoStreamFile

class AudioFile(BaseAudioVideoStreamFile):
    """Аудиофайл"""

    def __init__(self, name: str, size: int, owner: str,
                 format: str, codec_type: str, bitrate: int, duration: float, **kwargs):
        super().__init__(name, size, owner, format, codec_type, bitrate, duration, **kwargs)

    def get_metadata(self) -> dict:
        base_meta = super().get_metadata()
        return base_meta