import utility
from music_item import MusicItem
from typing import List
from abc import ABC, abstractmethod

class TypesMusic(ABC):
    @abstractmethod
    def display_type(self):
        ...

    def __str__(self):
        return self.display_type()

class Rock(TypesMusic):
    def display_type(self):
        return "Rock"

class Pop(TypesMusic):
    def display_type(self):
        return "Pop"

class Song(MusicItem):
    def __init__(self, title: str, artist: List[str], length: int, type_music: TypesMusic):
        super().__init__(title, artist)
        self.length = length
        self._type = type_music

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    @utility.check_length
    def length(self, length: int) -> None:
        self._length = length

    @property
    def type(self) -> TypesMusic:
        return self._type

    @type.setter
    def type(self, type_music: TypesMusic) -> None:
        if not isinstance(type_music, TypesMusic):
            raise ValueError("...")
        self._type = type_music

    def play(self):
        return f"title: {self.title}, artist: {self.artist}, type: {self.type} : PLAY"

    def __str__(self):
        return f"title: {self.title}, artist: {self.artist}, length: {self.length}"
