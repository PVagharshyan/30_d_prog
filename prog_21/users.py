from songs import Song
from artists import Artist
from typing import *
import utility

class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.favorite_songs: List[Song] = []
        self.favorite_artists: List[Artist] = []

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        self._contact_info = value

    @property
    def favorite_songs(self) -> List[Song]:
        return self._favorite_songs

    @favorite_songs.setter
    def favorite_songs(self, songs: List[Song]):
        self._favorite_songs = songs

    @property
    def favorite_artists(self) -> List[Artist]:
        return self._favorite_artists

    @favorite_artists.setter
    def favorite_artists(self, artists: List[Artist]):
        self._favorite_artists = artists

    @utility.type_checking(Song)
    def add_favorite_song(self, song: Song):
        self.favorite_songs.append(song)

    @utility.type_checking(Artist)
    def add_favorite_artist(self, artist: Artist):
        self.favorite_artists.append(artist)

    def create_playlist(self, playlist_name: str, songs: List[Song]):
        if not isinstance(playlist_name, str) or not isinstance(list, songs):
            raise ValueError("...")
        for i in songs:
            if not isinstance(i, Song):
                raise ValueError("...")
        playlist = Playlist(playlist_name, songs)
        return playlist
