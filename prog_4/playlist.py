from songs import Song
import utility

class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.check_name
    def name(self, name: str) -> None:
        self._name = name

    def add_song(self, song: Song) -> None:
        if not isinstance(song, Song):
            raise ValueError("...")
        self._songs.append(song)
