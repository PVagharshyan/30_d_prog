from info import Info
from game import Game
import utility

class Developer:
    def __init__(self, name: str, contact_info: Info) -> None:
        self.name = name
        self.contact_info = contact_info

    def create_game(self, game: Game) -> None:
        print(f"{self.name} has created a new game: {game.get_description()}")

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
