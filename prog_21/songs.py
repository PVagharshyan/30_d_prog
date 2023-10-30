from artists import Artist
from typing import *
import utility

class Song:
    def __init__(self, title: str, artist: Artist, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration

    @property
    def title(self):
        return self._title

    @title.setter
    @utility.type_checking(str)
    def title(self, value: str):
        self._title = value

    @property
    def artist(self):
        return self._artists

    @artist.setter
    @utility.type_checking(Artist)
    def artist(self, value: Artist):
        self._artists = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    @utility.type_checking(int)
    def duration(self, value: int):
        self._duration = value
