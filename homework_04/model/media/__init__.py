# homework_04/model/media/__init__.py
from .photo_file import PhotoFile
from .audio_file import AudioFile
from .video_file import VideoFile
from .file_registry import register_file_type

register_file_type(PhotoFile)
register_file_type(AudioFile)
register_file_type(VideoFile)