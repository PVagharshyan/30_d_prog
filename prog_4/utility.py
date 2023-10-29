from functools import wraps
from typing import List

def check_title(func):
    @wraps(func)
    def inner(self, title: str) -> None:
        if not isinstance(title, str):
            raise ValueError("...")
        return func(self, title)
    return inner

def check_artists(func):
    @wraps(func)
    def inner(self, artist: List[str]):
        if not isinstance(artist, list):
            raise ValueError("...")
        for i in artist:
            if not isinstance(i, str):
                raise ValueError("...")
        return func(self, artist)
    return inner

def check_length(func):
    @wraps(func)
    def inner(self, length: int) -> None:
        if not isinstance(length, int):
            raise ValueError("...")
        return func(self, length)
    return inner

def check_release_data(func):
    @wraps(func)
    def inner(self, release_data: int) -> None:
        if not isinstance(release_data, int) or release_data < 1950 or release_data > 2022:
            raise ValueError("...")
        return func(self, release_data)
    return inner

def check_name(func):
    @wraps(func)
    def inner(self, name: str) -> None:
        if not isinstance(name, str):
            raise ValueError("...")
        return func(self, name)
    return inner

