from homework_04.model.storage.cloud_storage import CloudStorage
from model.media.photo_file import PhotoFile
from model.media.audio_file import AudioFile
from model.media.video_file import VideoFile
from model.storage.local_storage import LocalStorage
from model.storage.ftp_storage import FtpStorage

# создаём файлы
my_favorit_song = AudioFile(
    name="my_fav_song",
    size=4000,
    owner="Andrey",
    format="mp3",
    codec_type="mp3",
    bitrate=320,
    duration=180
)

my_favorit_movie = VideoFile(
    name="my_fav_movie",
    size=500000,
    owner="Vasy",
    format="mp4",
    codec_type="H.264",
    bitrate=4000,
    duration=7200,
    resolution="1920x1080"
)

my_favorit_photo = PhotoFile(
        name="my_fav_image",
        size=2048,
        owner="Goga",
        format="jpg",
        resolution="4000x3000",
        camera_model="Canon EOS 5D"
    )

# используем хранилища
local_storage = LocalStorage()

ftp_storage = FtpStorage(
    host="localhost",
    port=21,
    user_name="user",
    password="pa$$" 
    )

cloud_storage = CloudStorage(
    host="localhost",
    user_name="user",
    password="pa$$" 
    )

local_storage.save(my_favorit_song)
ftp_storage.save(my_favorit_movie)

cloud_storage.save(my_favorit_photo)
my_last_image = cloud_storage.load("my_last_image")
if isinstance(my_last_image, PhotoFile):
    my_last_image.resize("1920x1080")

# действия над файлами
my_favorit_song.convert_format("wav")

photo_from_movie = my_favorit_movie.extract_frame(42.0)
crop_from_photo_from_movie = photo_from_movie.crop(10, 10, 20, 20)

# удаление
ftp_storage.delete(my_favorit_movie)
