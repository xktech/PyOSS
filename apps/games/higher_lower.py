import random

def higher_lower_game(low=1, high=100, max_attempts=10):
    target = random.randint(low, high)
    attempts = 0

    print(f"Guess a number between {low} and {high}!")

    while attempts < max_attempts:
        attempts += 1
        guess = int(input(f"Attempt {attempts}/{max_attempts}: "))

        if guess == target:
            print(f"Correct! The number was {target}.")
            return True
        elif guess < target:
            print("Higher!")
        else:
            print("Lower!")