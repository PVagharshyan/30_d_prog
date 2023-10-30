from typing import List
import utility

class Review:
    def __init__(self, rating: int, comments: str):
        self.rating = rating
        self.comments = comments

    @property
    def rating(self):
        return self._rating

    @rating.setter
    @utility.type_checking(int)
    def rating(self, value: int):
        self._rating = value

    @property
    def comments(self):
        return self._comments

    @comments.setter
    @utility.type_checking(str)
    def comments(self, value: str):
        self._comments = value

