from abc import ABC, abstractmethod
from typing import List
import utility
import copy

class MusicItem(ABC):
    def __init__(self, title, artist):
        self.artist = artist
        self.title = title

    @abstractmethod
    def play(self):
        ...

    @property
    def artist(self) -> List[str]:
        return copy.deepcopy(self._artist)

    @artist.setter
    @utility.check_artists
    def artist(self, new_artists: List[str]) -> None:
        self._artist = copy.deepcopy(new_artists)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    @utility.check_title
    def title(self, new_title: str) -> None:
        self._title = new_title
