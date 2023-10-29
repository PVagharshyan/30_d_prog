from songs import Song
from music_item import MusicItem
from typing import List
import copy
import utility

class Albom(MusicItem):
    def __init__(self, title: str, artist: List[str], release_data: int) -> None:
        super().__init__(title, artist)
        self.release_data = release_data
        self._songs = []

    def play(self) -> str:
        result = ""
        for i in self._songs:
            result += i.play() + "\n"
        return result

    def add_song(self, song: Song) -> None:
        if not isinstance(song, Song):
            raise ValueError("...")
        self._songs.append(song)

    @property
    def songs(self) -> str:
        result = ""
        for i in self._songs:
            result += str(i) + "\n"
        return result

    @property
    def release_data(self) -> int:
        return self._release_data

    @release_data.setter
    @utility.check_release_data
    def release_data(self, release_data):
        self._release_data = release_data
