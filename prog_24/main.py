from abc import ABC, abstractmethod
from typing import List
from games import Game, SportsGame, AdventureGame
from players import Player
from consoles import Console, XboxConsole, PlayStationConsole


def main():
    player1 = Player("Alice", "alice@example.com")
    player2 = Player("Bob", "bob@example.com")
    football_game = SportsGame("FIFA 22", "2022-09-10")
    adventure_game = AdventureGame("The Legend of Zelda", "2022-07-20")

    xbox = XboxConsole()
    playstation = PlayStationConsole()

    xbox.installed_games.append(football_game)
    playstation.installed_games.append(adventure_game)

    xbox.play_game(player1, football_game)
    playstation.play_game(player2, adventure_game)

    xbox.compete_with_player(player1, player2, football_game)
    playstation.save_game_progress(player1, adventure_game)

if __name__ == "__main__":
    main()
