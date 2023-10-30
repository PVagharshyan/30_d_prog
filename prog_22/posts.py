from abc import ABC, abstractmethod
from users import User
from datetime import datetime
from comments import Comment
from typing import List
import utility

class Post(ABC):
    def __init__(self, user: User, content: str):
        self.user = user
        self.content = content
        self._timestamp = datetime.now()
        self._comments: List['Comment'] = []

    @property
    def user(self):
        return self._user

    @user.setter
    @utility.type_checking(User)
    def user(self, value: User):
        self._user = value

    @property
    def content(self):
        return self._content

    @content.setter
    @utility.type_checking(str)
    def content(self, value: str):
        self._content = value

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def comments(self):
        return self._comments

    @comments.setter
    @utility.container_type_checking(list, comments)
    def comments(self, value: List['Comment']):
        self._comments = value

    @abstractmethod
    def display(self):
        pass

class TextPost(Post):
    def __init__(self, user: User, content: str):
        super().__init__(user, content)

    def display(self):
        return f"{self.user.name} posted a text: {self.content}"

class PhotoPost(Post):
    def __init__(self, user: User, content: str, image_url: str):
        super().__init__(user, content)
        self.image_url = image_url

    def display(self):
        return f"{self.user.name} posted a photo: {self.content} ({self.image_url})"
