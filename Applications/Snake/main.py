from game.game import Game


def main():
    
    is_game: bool = True
    while is_game:
        game = Game()
        is_game = game.run_game()

if __name__ == "__main__":
    main()