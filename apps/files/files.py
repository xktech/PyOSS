import time
import os
import json
from core.utils import new_window
import core.config as config


def files():
    new_window(config.username)

    os.makedirs("users", exist_ok=True)

    SAVE_FILE = f"users/{config.username}_files.json"

    default_fs = {
        "home": {
            "notes.txt": "Hello World!",
            "games": {},
            "system": {
                "config.sys": "darkmode=true"
            }
        }
    }

    # LOAD FILESYSTEM
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            file_system = json.load(f)
    else:
        file_system = default_fs

        with open(SAVE_FILE, "w") as f:
            json.dump(file_system, f, indent=4)

    # SAVE FUNCTION
    def save_fs():
        with open(SAVE_FILE, "w") as f:
            json.dump(file_system, f, indent=4)

    path = ["home"]

    def get_current_dir():
        current = file_system
        for folder in path:
            current = current[folder]
        return current

    def pwd():
        return "/" + "/".join(path)

    print("You are in the home directory.")
    print("Commands: ls, cd <folder>, cd .., pwd, exit, cat, mkdir, touch, rm")

    while True:
        cmd = input("> ").strip()
        parts = cmd.split()

        if len(parts) == 0:
            continue

        command = parts[0]

        # EXIT
        if command == "exit":
            print("Exiting...")
            time.sleep(1)
            break

        # LS
        elif command == "ls":
            current = get_current_dir()
            for item in current:
                print(item)

        # PWD
        elif command == "pwd":
            print(pwd())

        # CD
        elif command == "cd":
            if len(parts) < 2:
                print("Usage: cd <folder> or cd ..")
                continue

            target = parts[1]
            current = get_current_dir()

            if target == "..":
                if len(path) > 1:
                    path.pop()
            elif target in current and isinstance(current[target], dict):
                path.append(target)
            else:
                print("Folder not found")
        
        # CAT
        elif command == "cat":
            if len(parts) < 2:
                print("Usage: cat <file>")
                continue

            filename = parts[1]
            current = get_current_dir()

            if filename in current and isinstance(current[filename], str):
                print(current[filename])
            else:
                print("File not found.")


        # MKDIR
        elif command == "mkdir":
            if len(parts) < 2:
                print("Usage: mkdir <path>")
                return

            parts_path = parts[1].split("/")
            folder = get_current_dir()

            for p in parts_path[:-1]:
                if p not in folder or not isinstance(folder[p], dict):
                    print(f"mkdir: cannot create '{parts[1]}': No such directory")
                    return
                folder = folder[p]

            new_dir = parts_path[-1]

            if new_dir in folder:
                print("mkdir: File exists")
                return

            folder[new_dir] = {}
            save_fs()
            print(f"Created folder: {parts[1]}")

        # TOUCH
        elif command == "touch":
            if len(parts) < 2:
                print("Usage: touch <filename>")
                return
            
            filename = parts[1]
            folder = get_current_dir()

            if filename in folder:
                print(f"touch: '{filename}' already exists")
                return
            
            folder[filename] = ""
            save_fs()
            print(f"Touched: {filename}")


        # RM
        elif command == "rm":
            if len(parts) < 2:
                print("Usage: rm <file/folder>")
                return
            
            name = parts[1]
            folder = get_current_dir()

            if name not in folder:
                print(f"rm: cannot remove '{name}': No such file or directory.")
                return
            
            del folder[name]
            save_fs()
            print(f"Removed: {name}")

        # EDIT FILES
        elif command == "edit":
            if len(parts) < 2:
                print("Usage: edit <filename>")
                return
            
            filename = parts[1]
            folder = get_current_dir()

            if filename not in folder:
                print(f"edit: '{filename}' does not exist.")
                return
            
            print("\n--- EDIT MODE ---")
            print("Type your content below.")
            print("Type ':sq' to save and quit.")
            print("NOTE: It erases the current contents of the file. You will have to")
            print("re-write it again. This is a bug but not an important one currently\n")

            print(f"Current content: \n{folder[filename]}\n")


            lines = []

            while True:
                line = input()

                if line == ":sq":
                    break

                lines.append(line)

            folder[filename] = "\n".join(lines)
            save_fs()
            print(f"Saved: {filename}")