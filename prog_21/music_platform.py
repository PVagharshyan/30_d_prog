from songs import Song
from artists import Artist
from typing import *
import utility
import copy

class MusicPlatform:
    def __init__(self):
        self._songs: List[Song] = []
        self._artists: List[Artist] = []

    @utility.type_checking(Song)
    def add_song(self, song: Song):
        self._songs.append(song)
        self._artists.append(song.artist)

    @utility.type_checking(str)
    def search_song(self, title: str) -> Song:
        for song in self._songs:
            if title.lower() in song.title.lower():
                return song
        return None

    def discover_artist(self) -> List[Artist]:
        return copy.deepcopy(self._artists)

class RockSong(Song):
    def __init__(self, title: str, artist: Artist, duration: int, subgenre: str):
        super().__init__(title, artist, duration)
        self.subgenre = subgenre

    @property
    def subgenre(self):
        return self._subgenre

    @subgenre.setter
    @utility.type_checking(str)
    def subgenre(self, value: str):
        self._subgenre = value

class PopSong(Song):
    def __init__(self, title: str, artist: Artist, duration: int, mood: str):
        super().__init__(title, artist, duration)
        self.mood = mood

    @property
    def mood(self):
        return self._mood

    @mood.setter
    @utility.type_checking(str)
    def mood(self, value: str):
        self._mood = value
