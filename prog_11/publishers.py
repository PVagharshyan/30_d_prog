from info import Info
from game import Game
import utility

class Publisher:
    def __init__(self, name: str, contact_info: Info):
        self.name = name
        self.contact_info = contact_info

    @utility.type_checking(Game)
    def release_game(self, game: Game) -> None:
        print(f"{self.name} has released a new game: {game.get_description()}")

    @utility.type_checking(Game, str)
    def sell_game(self, game: Game, customer: str) -> None:
        print(f"{customer} has purchased {game.get_description()} from {self.name}")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, name: str) -> None:
        self._name = name

    @property
    def contact_info(self) -> Info:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(Info)
    def contact_info(self, contact_info: Info) -> None:
        self._contact_info = contact_info

