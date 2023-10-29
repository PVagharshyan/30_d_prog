from abc import ABC, abstractmethod
import utility

class Game(ABC):
    def __init__(self, title: str, genre: str, release_date: str):
        self.title = title
        self.genre = genre
        self.release_date = release_date

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    @utility.type_checking(str)
    def title(self, title: str) -> None:
        self._title = title

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    @utility.type_checking(str)
    def genre(self, genre: str) -> None:
        self._genre = genre

    @property
    def release_date(self) -> str:
        return self._release_date

    @release_date.setter
    def release_date(self, release_date: str) -> None:
        utility.check_data(release_date)
        self._release_date = release_date

class ActionGame(Game):
    def __init__(self, title: str, release_date: str, difficulty_level: str):
        super().__init__(title, "Action", release_date)
        self.difficulty_level = difficulty_level

    def play(self) -> None:
        print(f"Playing {self.title} - Action game at {self.difficulty_level} difficulty level.")

    def get_description(self) -> str:
        return f"{self.title} - Action game ({self.release_date})"

    @property
    def difficulty_level(self) -> str:
        return self._difficulty_level

    @difficulty_level.setter
    @utility.type_checking(str)
    def difficulty_level(self, value: str) -> None:
        self._difficulty_level = value

class StrategyGame(Game):
    def __init__(self, title: str, release_date: str, complexity_level: str):
        super().__init__(title, "Strategy", release_date)
        self.complexity_level = complexity_level

    def play(self) -> None:
        print(f"Playing {self.title} - Strategy game with a complexity level of {self.complexity_level}.")

    def get_description(self) -> str:
        return f"{self.title} - Strategy game ({self.release_date})"

    @property
    def complexity_level(self) -> str:
        return self._complexity_level

    @complexity_level.setter
    @utility.type_checking(str)
    def complexity_level(self, value: str) -> None:
        self._complexity_level = value

