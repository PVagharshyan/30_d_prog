from datetime import datetime
from typing import List, Optional
from comments import Comment, User_c
from posts import Post, User_p
import utility

class User(User_c, User_p):
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self._posts: List[Post] = []
        self._comments: List[Comment] = []

    @utility.type_checking(str, type)
    def create_post(self, post_content: str, post_type: type) -> Post:
        post = post_type(self, post_content)
        self._posts.append(post)
        return post

    @utility.type_checking(Post, str)
    def leave_comment(self, post: Post, comment_content: str) -> Comment:
        comment = Comment(self, post, comment_content)
        post.add_comment(comment)
        self._comments.append(comment)

    def view_posts(self) -> None:
        for post in self._posts:
            print(post)

    def update_profile(self, new_name: str, new_contact_info: str) -> None:
        self.name = new_name
        self.contact_info = new_contact_info

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, name: str) -> None:
        self._name = name

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        self._contact_info = value

    def __str__(self) -> str:
        return f"User: {self.name}"
