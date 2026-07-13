import time
import sys
from colorama import init, Fore, Style

from core.utils import print_centered
import core.config as config
from core.utils import new_window
import platform
import psutil


un = config.username

def systemSpecs():
    new_window(config.username)
    while True:
        print("System:", platform.system())
        print("Release:", platform.release())
        print("Version:", platform.version())
        print("Machine:", platform.machine())
        print("Processor:", platform.processor())

        print("CPU Cores:", psutil.cpu_count(logical=True))
        print("RAM GB:", round(psutil.virtual_memory().total / (1024**3), 2))
        
        break

def shutdown():
    new_window(un)
    print_centered(Fore.RED + "Shutting down..")
    print_centered()
    time.sleep(1)
    print_centered(Fore.CYAN + f"Goodbye {config.username}!") # TODO: Fix
    print_centered()
    time.sleep(0.5)
    sys.exit(0)
