from developers import Developer
from game import Game, ActionGame, StrategyGame
from info import Info
from publishers import Publisher

if __name__ == "__main__":
    i = Info("039393939", "asdasfds", "dev@email.com")
    developer = Developer("GameDevCo", i)
    action_game = ActionGame("Action Game 1", "2023-10-28", "Hard")
    developer.create_game(action_game)

    i = Info("039393939", "asdasfds", "pub@email.com")
    publisher = Publisher("GamePublisherCo", i)
    publisher.release_game(action_game)
    publisher.sell_game(action_game, "Player123")

    strategy_game = StrategyGame("Strategy Game 1", "2023-10-29", "Advanced")
    developer.create_game(strategy_game)
    publisher.release_game(strategy_game)
    publisher.sell_game(strategy_game, "Player456")

    action_game.play()
    strategy_game.play()
