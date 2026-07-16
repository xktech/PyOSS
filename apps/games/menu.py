from .rng import random_number_game
from .rps import rps
from .pong import pong
from .higher_lower import higher_lower_game
from .text_adventure import text_adventure
from .quiz import quiz


def render_games():
    print("-" * 38)
    print("1. Number Game")
    print("2. Rock Paper Scissors")
    print("3. Higher or Lower")
    print("4. Pong")
    print("5. Text Adventure (WIP. NOT DONE)")
    print("6. QUIZ")
    print("7. Type 'back' to return")
    print("-" * 38)


def games_menu():
    while True:
        render_games()
        
        gameChoice = input(">> ")

        if gameChoice == "1":
            random_number_game()

        elif gameChoice == "2":
            rps()

        elif gameChoice == "3":
            higher_lower_game()

        elif gameChoice == "4":
            pong()

        elif gameChoice == "5":
            text_adventure()
            pass
        elif gameChoice():
            quiz()
        elif gameChoice == "back":
            break