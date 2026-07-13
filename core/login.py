import json
import os
import getpass
import core.config as config

USERS_FILE = "data/users/users.json"
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)
def register_user():
    print("\n--- REGISTER NEW USER ---")

    users = load_users()

    while True:
        username = input("Choose username: ").strip()

        if username in users:
            print("Username already exists. Try another.")
            continue
        if username == "":
            print("Username cannot be empty / have spaces in.")
            continue
        break

    while True:
        password = input("Create password: ").strip()

        if len(password) < 3:
            print("Password too short (min 3 chars).")
            continue
        break

    users[username] = password
    save_users(users)

    print(f"\nUser '{username}' created successfully!")
    return username