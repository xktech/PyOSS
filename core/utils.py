import shutil
import winsound
from colorama import Fore, Style

# NUMBER
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


# TEXT
def center_text(text=""):
    width = shutil.get_terminal_size().columns
    return text.center(width)

def print_centered(text=""):
    print(center_text(text))

def center_block(text):
    """Centers a multi-line block (like ASCII art) as one unit,
    so internal alignment isn't destroyed."""
    width = shutil.get_terminal_size().columns
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    pad = max(0, (width - max_len) // 2)
    return "\n".join((" " * pad) + line for line in lines)

def center_input_prompt(text=""):
    """Like center_text, but for use with input() —
    only pads on the left, so the cursor lands in the middle,
    not pushed off to the right by trailing spaces."""
    width = shutil.get_terminal_size().columns
    pad = max(0, (width - len(text)) // 2)
    return " " * pad + text

# SCREEN
def new_window(username):
    print("\033c", end="")  # Clear screen
    print(Style.RESET_ALL)

# SOUNDS
def error_sound():
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
def success_sound():
    winsound.Beep(800, 100)