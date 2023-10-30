from games import Game
from players import Player
from abc import abstractmethod, ABC
import utility

class Console(ABC):
    def __init__(self, console_type: str):
        self.console_type = console_type
        self.installed_games: List[Game] = []

    @property
    def console_type(self):
        return self._console_type

    @console_type.setter
    @utility.type_checking(str)
    def console_type(self, value: str):
        self._console_type = value

    @abstractmethod
    def play_game(self, player: Player, game: Game):
        pass

    @abstractmethod
    def save_game_progress(self, player: Player, game: Game):
        pass

    @abstractmethod
    def compete_with_player(self, player1: Player, player2: Player, game: Game):
        pass

class XboxConsole(Console):
    def __init__(self):
        super().__init__("Xbox")

    def play_game(self, player: Player, game: Game):
        if game in self.installed_games:
            print(f"{player.name} is playing {game.title} on Xbox.")

    def save_game_progress(self, player: Player, game: Game):
        print(f"{player.name} is saving the progress of {game.title} on Xbox.")

    def compete_with_player(self, player1: Player, player2: Player, game: Game):
        print(f"{player1.name} is competing with {player2.name} in {game.title} on Xbox.")

class PlayStationConsole(Console):
    def __init__(self):
        super().__init__("PlayStation")

    def play_game(self, player: Player, game: Game):
        if game in self.installed_games:
            print(f"{player.name} is playing {game.title} on PlayStation.")

    def save_game_progress(self, player: Player, game: Game):
        print(f"{player.name} is saving the progress of {game.title} on PlayStation.")

    def compete_with_player(self, player1: Player, player2: Player, game: Game):
        print(f"{player1.name} is competing with {player2.name} in {game.title} on PlayStation.")
