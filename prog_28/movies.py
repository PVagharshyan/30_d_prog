import utility

class Movie:
    def __init__(self, title: str, genre: str, length: int):
        self.title = title
        self.genre = genre
        self.length = length

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    @utility.type_checking(str)
    def title(self, new_title: str):
        self._title = new_title

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    @utility.type_checking(str)
    def genre(self, new_genre: str):
        self._genre = new_genre

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    @utility.type_checking(int)
    def length(self, new_length: int):
        if new_length >= 0:
            self._length = new_length
        else:
            raise ValueError("Length must be non-negative")
