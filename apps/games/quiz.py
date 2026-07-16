import random
import json
import os
import core.config as config

def get_games_file():
    return f"users/{config.username}/games.json"

def setup():
    games_file = get_games_file()

    os.makedirs(f"users/{config.username}", exist_ok=True)

    if not os.path.exists(games_file):
        with open(games_file, "w") as f:
            json.dump(DEFAULT_DATA, f, indent=4)

DEFAULT_DATA = {
    "quiz": {
        "games_played": 0,
        "wins": 0,
        "high_score": 0,
        "total_score": 0
    }
}

games_file = get_games_file()


def load_score():
    with open(get_games_file(), "r") as f:
        return json.load(f)


def save_score(data):
    with open(get_games_file(), "w") as f:
        json.dump(data, f, indent=4)


questions = {
    "What Does CPU Stand for?": "central processing unit",
    "What Does GPU Stand for?": "graphics processing unit",
    "What Does RAM Stand for?": "random access memory",
    "What Does ROM Stand for?": "read only memory",
    "What Does SSD Stand for?": "solid state drive",
    "What Does HDD Stand for?": "hard disk drive",
    "What Does USB Stand for?": "universal serial bus",
    "What Does HDMI Stand for?": "high definition multimedia interface",
    "What Does LAN Stand for?": "local area network",
    "What Does WAN Stand for?": "wide area network",
    "What Does Wi-Fi Stand for?": "wireless fidelity",
    "What Does URL Stand for?": "uniform resource locator",
    "What Does HTTP Stand for?": "hypertext transfer protocol",
    "What Does HTTPS Stand for?": "hypertext transfer protocol secure",
    "What Does HTML Stand for?": "hypertext markup language",
    "What Does CSS Stand for?": "cascading style sheets",
    "What Does OS Stand for?": "operating system",
    "What Does GUI Stand for?": "graphical user interface",
    "What Does CLI Stand for?": "command line interface",
    "What Does BIOS Stand for?": "basic input output system",
    "What Does UEFI Stand for?": "unified extensible firmware interface",
    "What Does PSU Stand for?": "power supply unit",
    "What Does FPS Stand for?": "frames per second",
    "What Does DNS Stand for?": "domain name system",
    "What Does VPN Stand for?": "virtual private network",
    "What Does AI Stand for?": "artificial intelligence",
    "What Does API Stand for?": "application programming interface",
    "What Does JSON Stand for?": "javascript object notation",
    "What Does XML Stand for?": "extensible markup language",
    "What Does SQL Stand for?": "structured query language",
    "What Does PDF Stand for?": "portable document format",
    "What Does PNG Stand for?": "portable network graphics",
    "What Does JPEG Stand for?": "joint photographic experts group",
    "What Does GIF Stand for?": "graphics interchange format",
    "What Does APK Stand for?": "android package kit",
    "What Does IDE Stand for?": "integrated development environment",
    "What Does DNS do?": "translates domain names into ip addresses",
    "Which company created Windows?": "microsoft",
    "Which company created Linux?": "linus torvalds",
    "Which company created macOS?": "apple",
    "Which company develops Python?": "python software foundation",
    "Which key is commonly used to refresh a webpage?": "f5",
    "Which operating system is open source and based on Unix?": "linux",
    "Which component performs calculations in a computer?": "cpu",
    "Which component stores data permanently?": "storage",
    "Which component is known as temporary memory?": "ram",
    "Is RAM volatile or non-volatile?": "volatile",
    "Is ROM volatile or non-volatile?": "non-volatile",
    "Is SSD storage volatile or non-volatile?": "non-volatile",
    "Binary uses which two digits?": "0 and 1",
    "How many bits are in one byte?": "8",
    "What is the largest unit? KB, MB, GB or TB?": "tb",
    "What file extension do Python files use?": ".py",
    "What file extension do text files use?": ".txt",
    "What symbol starts a comment in Python?": "#",
    "Which Python function displays text?": "print",
    "Which Python function gets user input?": "input",
    "Which Python data type stores true or false?": "boolean",
    "Which Python keyword creates a function?": "def",
    "What loop repeats while a condition is true?": "while",
    "What loop iterates over a sequence?": "for",
    "What keyword exits a loop?": "break",
    "What keyword skips to the next loop iteration?": "continue",
    "What does Ctrl+C usually do in a terminal?": "interrupts the current program",
    "Which command lists files in Linux?": "ls",
    "Which command changes directory in Linux?": "cd",
    "Which command creates a new directory in Linux?": "mkdir",
    "Which command removes a file in Linux?": "rm",
    "Which command prints the current directory?": "pwd"
}


def play():
    setup()
    score = 0

    question, answer = random.choice(list(questions.items()))

    user_answer = input(f"\n{question}\n> ").strip().lower()

    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        score += 1
        
    else:
        print(f"Wrong! The answer was: {answer}")

    print(f"Score: {score}")

    games = load_score()

    games["quiz"]["games_played"] += 1
    games["quiz"]["total_score"] += score

    if score > games["quiz"]["high_score"]:
        games["quiz"]["high_score"] = score

    if score == 1:
        games["quiz"]["wins"] += 1

    save_score(games)


def check_score():
    games = load_score()
    quiz = games["quiz"]

    print("\n------ QUIZ STATS ------")
    print(f"Games Played : {quiz['games_played']}")
    print(f"Wins         : {quiz['wins']}")
    print(f"High Score   : {quiz['high_score']}")
    print(f"Total Score  : {quiz['total_score']}")
    print("------------------------")


def render_quiz():
    print("-" * 38)
    print("1. Play")
    print("2. Check Score")
    print("3. Exit")
    print("-" * 38)


def quiz():
    while True:
        render_quiz()

        choice = input(">> ").strip()

        if choice == "1":
            play()
        elif choice == "2":
            check_score()
        elif choice == "3":
            break
        else:
            print("Please choose a number from the list.")