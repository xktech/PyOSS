import core.config as config
from apps.calculator import calculator
from apps.music import music
from apps.files.files import files
from apps.notes import notes
from apps.games.menu import games_menu
from apps.school.school import school_menu
from core.menu import render_home
from core.system import systemSpecs
from core.system import shutdown
from core.utils import new_window

un = config.username

def homepage():
    while True:
        render_home()

        homeChoice = input(">> ").lower().strip()
        if homeChoice == "files":
            files()
            new_window(un)


        # SYSTEM
        elif homeChoice == "system specs":
            systemSpecs()
            new_window(un)
        
        elif homeChoice == "games":
            new_window(un)
            games_menu()
            new_window(un)

        elif homeChoice == "school":
            new_window(un)
            school_menu()
            new_window(un)

        # OTHER
        elif homeChoice == "calculator":
            calculator()
            new_window(un)

        elif homeChoice == "notes":
            notes()
            new_window(un)

        elif homeChoice == "music":
            music()
            new_window(un)


        # EXIT 
        elif homeChoice == "logout":
            break
        elif homeChoice == "shutdown":
            shutdown()