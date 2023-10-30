import utility

class Game:
    def __init__(self, title: str, genre: str, release_date: str):
        self.title = title
        self.genre = genre
        self.release_date = release_date

    @property
    def title(self):
        return self._title

    @title.setter
    @utility.type_checking(str)
    def title(self, new_title):
        self._title = new_title

    @property
    def genre(self):
        return self._genre

    @genre.setter
    @utility.type_checking(str)
    def genre(self, new_genre):
        self._genre = new_genre

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    @utility.type_checking(str)
    def release_date(self, new_release_date):
        self._release_date = new_release_date

class SportsGame(Game):
    def __init__(self, title: str, release_date: str):
        super().__init__(title, "Sports", release_date)

class AdventureGame(Game):
    def __init__(self, title: str, release_date: str):
        super().__init__(title, "Adventure", release_date)
