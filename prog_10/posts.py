from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
import utility
import copy

class User_p:
    ...

class Comment_p:
    ...

class Post(ABC):
    def __init__(self, user: User_p, content: str):
        self.user = user
        self.content = content
        self._timestamp = datetime.now()
        self._comments: List['Comment_p'] = []

    @abstractmethod
    def post_type(self) -> str:
        pass

    @utility.type_checking(Comment_p)
    def add_comment(self, comment: Comment_p) -> None:
        self._comments.append(comment)

    def __str__(self) -> str:
        return f"{self.post_type()} Post by {self.user.name} ({self.timestamp}):\n{self.content}"

    @property
    def user(self) -> User_p:
        return self._user

    @user.setter
    @utility.type_checking(User_p)
    def user(self, user: User_p) -> None:
        self._user = user

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    @utility.type_checking(str)
    def content(self, content: str) -> None:
        self._content = content

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def comments(self):
        return copy.deepcopy(self._comments)

class TextPost(Post):
    def post_type(self) -> str:
        return "Text"

class ImagePost(Post):
    def post_type(self) -> str:
        return "Image"
