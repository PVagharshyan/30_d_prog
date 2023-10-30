from songs import Song
from typing import *
import utility

class Playlist:
    def __init__(self, name: str, songs: List[Song]):
        self.name = name
        self.songs = songs

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def songs(self):
        return self._songs

    @songs.setter
    @utility.type_checking(Song)
    def songs(self, value: Song):
        self._songs = value

