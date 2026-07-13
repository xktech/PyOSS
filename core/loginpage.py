import getpass
import bcrypt

from core.utils import new_window
from core.utils import print_centered
from core.utils import center_input_prompt
from core.boot import boot_screen
from core.login import load_users
from core.login import register_user
from core.home import homepage
from assets.sounds.sounds import success_sound
from assets.sounds.sounds import error_sound
import core.config as config


def loginpage():
    while True:
        new_window("Guest")
        boot_screen()
        print_centered("LOGIN SCREEN")
        print_centered()
        print_centered("New user or existing user?")
        print_centered()
        print_centered("If you are an existing user, please enter your username.")
        print_centered()
        print_centered("Press Q to shutdown")
        print_centered()

        choice = input(center_input_prompt("> ")).strip()

        if choice == "new":
            username = register_user()
            homepage(username)

        elif choice == "q":
            break

        else:
            users = load_users()
            username = choice.strip()

            if username in users:
                password = getpass.getpass(center_input_prompt("Password: "))

                stored_hash = users[username]

                if bcrypt.checkpw(
                    password.encode("utf-8"),
                    stored_hash.encode("utf-8")
                ):
                    success_sound()
                    config.username = username
                    homepage(username)
                else:
                    error_sound()
                    print("Wrong password.")
            else:
                error_sound()
                print("User not found.")