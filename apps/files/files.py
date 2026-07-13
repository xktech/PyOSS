import os
import json
import time

import core.config as config
from core.utils import new_window


USER_DIR = "users"


def get_save_file():
    os.makedirs(USER_DIR, exist_ok=True)
    return os.path.join(USER_DIR, f"{config.username}_files.json")


def create_default_filesystem():
    return {
        "home": {
            "notes.txt": "Note from the dev: Welcome to PyOSS!\n"
            "Join my discord server: (link) for any FAQ's or bugs\n"
            "There are currently a ton of bugs that i will have to fix\n"
            "but i hope you enjoy!",
            "games": {},
            "system": {
                "config.sys": "darkmode=true"
            }
        }
    }


def load_filesystem():
    save_file = get_save_file()

    if os.path.exists(save_file):
        try:
            with open(save_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Filesystem corrupted. Creating a new one.")

    filesystem = create_default_filesystem()

    with open(save_file, "w") as f:
        json.dump(filesystem, f, indent=4)

    return filesystem


def save_filesystem(filesystem):
    with open(get_save_file(), "w") as f:
        json.dump(filesystem, f, indent=4)


def files():
    new_window(config.username)

    filesystem = load_filesystem()

    path = ["home"]


    def current_directory():
        folder = filesystem

        for item in path:
            folder = folder[item]

        return folder


    def current_path():
        return "/" + "/".join(path)


    print(f"Welcome {config.username}'s filesystem")
    print("Commands:")
    print("ls | cd <folder> | cd .. | pwd | cat <file>")
    print("mkdir <folder> | touch <file> | edit <file>")
    print("rm <file/folder> | exit")


    while True:
        command = input(f"{current_path()} > ").strip()

        if not command:
            continue


        args = command.split()
        cmd = args[0]


        # EXIT
        if cmd == "exit":
            print("Saving filesystem...")
            save_filesystem(filesystem)
            time.sleep(1)
            break


        # LIST FILES
        elif cmd == "ls":
            for item in current_directory():
                print(item)


        # PRINT CURRENT PATH
        elif cmd == "pwd":
            print(current_path())


        # CHANGE DIRECTORY
        elif cmd == "cd":

            if len(args) < 2:
                print("Usage: cd <folder>")
                continue

            target = args[1]


            if target == "..":

                if len(path) > 1:
                    path.pop()

                continue


            folder = current_directory()

            if target in folder and isinstance(folder[target], dict):
                path.append(target)

            else:
                print("Folder not found.")



        # READ FILE
        elif cmd == "cat":

            if len(args) < 2:
                print("Usage: cat <file>")
                continue

            filename = args[1]
            folder = current_directory()


            if filename in folder and isinstance(folder[filename], str):
                print(folder[filename])

            else:
                print("File not found.")



        # CREATE FOLDER
        elif cmd == "mkdir":

            if len(args) < 2:
                print("Usage: mkdir <folder>")
                continue

            name = args[1]
            folder = current_directory()


            if name in folder:
                print("Already exists.")
                continue


            folder[name] = {}

            save_filesystem(filesystem)

            print(f"Created folder: {name}")



        # CREATE FILE
        elif cmd == "touch":

            if len(args) < 2:
                print("Usage: touch <file>")
                continue

            filename = args[1]
            folder = current_directory()


            if filename in folder:
                print("File already exists.")
                continue


            folder[filename] = ""

            save_filesystem(filesystem)

            print(f"Created file: {filename}")



        # DELETE FILE/FOLDER
        elif cmd == "rm":

            if len(args) < 2:
                print("Usage: rm <file/folder>")
                continue


            name = args[1]
            folder = current_directory()


            if name not in folder:
                print("Not found.")
                continue


            del folder[name]

            save_filesystem(filesystem)

            print(f"Removed: {name}")



        # EDIT FILE
        elif cmd == "edit":

            if len(args) < 2:
                print("Usage: edit <file>")
                continue


            filename = args[1]
            folder = current_directory()


            if filename not in folder:
                print("File does not exist.")
                continue


            print("\n--- EDIT MODE ---")
            print("Type :save to save\n")


            content = []


            while True:
                line = input()

                if line == ":save":
                    break

                content.append(line)


            folder[filename] = "\n".join(content)

            save_filesystem(filesystem)

            print("Saved.")



        else:
            print("Unknown command.")