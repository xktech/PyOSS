import random
from core.utils import get_number

def random_number_game():
    number = random.randint(1, 100)
    print("In this game. You guess a number (1 - 100 ('123' to leave))")
    while True:
        guess = get_number("Enter Your Guess: ")

        if guess == 123:
            break
        elif guess == number:
            print("You got it correct!")
            keep_going = input("Keep Going? (Y/N) ").lower()
            if keep_going == "y":
                number = random.randint(1, 100)  # reset the number
                continue
            elif keep_going == "n":
                break
            else:
                print("Only Y / N")
        else:
            print("You got it wrong!")