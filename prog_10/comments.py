from datetime import datetime
from typing import List, Optional
from posts import Post, Comment_p
import utility

class User_c:
    ...

class Comment(Comment_p):
    def __init__(self, user: User_c, post: Post, content: str) -> None:
        self.user = user
        self.post = post
        self.content = content

    @property
    def user(self) -> User_c:
        return self._user

    @user.setter
    @utility.type_checking(User_c)
    def user(self, value: User_c) -> None:
        self._user = value

    @property
    def post(self) -> Post:
        return self._post

    @post.setter
    @utility.type_checking(Post)
    def post(self, value: Post) -> None:
        self._post = value

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    @utility.type_checking(str)
    def content(self, value: str) -> None:
        self._content = value

    def __str__(self) -> str:
        return f"Comment by {self.user.name} on {self.post.post_type()} Post by {self.post.user.name}:\n{self.content}"

