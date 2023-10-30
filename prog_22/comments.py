from users import User
from datetime import datetime
import utility

class Comment:
    def __init__(self, user: User, content: str):
        self.user = user
        self.content = content
        self._timestamp = datetime.now()

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
