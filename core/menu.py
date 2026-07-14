from core.utils import new_window
import core.config as config

un = config.username

def render_home():  
    new_window(un)
    print("-" * 38)
    print("Files                      /GAMES")
    print("System Specs               /SCHOOL")
    print("Calculator                 Placeholder")
    print("Music                      Placeholder")
    print("Notes                      Placeholder")
    print("         Logout or Shutdown           ")
    print("-" * 38)


