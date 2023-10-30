from typing import List
from users import User
from posts import Post, TextPost, PhotoPost
from comments import Comment

class SocialMediaPlatform:
    def __init__(self):
        self.users: List[User] = []
        self.posts: List[Post] = []

    def create_user(self, name: str, contact_info: str):
        user = User(name, contact_info)
        self.users.append(user)
        return user

    def create_text_post(self, user: User, content: str):
        post = TextPost(user, content)
        self.posts.append(post)
        return post

    def create_photo_post(self, user: User, content: str, image_url: str):
        post = PhotoPost(user, content, image_url)
        self.posts.append(post)
        return post

    def add_comment(self, post: Post, user: User, content: str):
        comment = Comment(user, content)
        post.comments.append(comment)
