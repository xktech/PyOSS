import random

def rps():
    # Rock Paper Scissors
    OPTIONS = ['rock', 'paper', 'scissors']

    beats = {
            "paper":"rock",
            "scissors":"paper",
            "rock":"scissors",
        }


    while True:
        ai_choice = random.choice(OPTIONS)
        
        human_choice = input("Rock, Paper or Scissors? (q to exit): ").lower()


        print(f"Your Choice: {human_choice}")
        print(f"AI Choice: {ai_choice}")

        if human_choice == "q":
            break
        else:
            if human_choice == ai_choice:
                print("TIE!")
            elif beats[human_choice] == ai_choice:
                print("You WIN!")
            else:
                print("AI Wins!")