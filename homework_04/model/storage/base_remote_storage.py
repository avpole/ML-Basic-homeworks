# homework_04/model/storage/base_remote_storage.py
from abc import ABC, abstractmethod
from .base_storage import BaseStorage


class BaseRemoteStorage(BaseStorage, ABC):
    """Локальное хранилище"""

    def __init__(self, host: str, user_name: str, password: str, do_connect: bool = True):
        self.host = host
        self.user_name = user_name
        self.password = password
        self._connected = False

        if do_connect:
            try:
                self.connect()
            except Exception:
                pass

    @abstractmethod
    def connect(self):
        """Установить соединение с сервером/облаком"""
        pass

    @abstractmethod
    def disconnect(self):
        """Разорвать соединение с сервером/облаком"""
        self._connected = False

    def __del__(self):
        """Деструктор: разрываем соединение при удалении объекта"""
        if getattr(self, "_connected", False):
            try:
                self.disconnect()
            except Exception:
                pass