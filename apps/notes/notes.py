from core.utils import new_window
from core.utils import get_number
import core.config as config

import json
import os
import datetime


def notes():
    new_window(config.username)
    NOTES_FILE = "notes.json"
    
    def loadNotes():
        if os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "r") as f:
                return json.load(f)
            return []
        
    notes = loadNotes()

    def saveNotes():
        with open(NOTES_FILE, "w") as f:
            json.dump(notes, f, indent=2)

    def viewNotes():
        if not notes:
            print("No notes to display!")
            return

        print("\n--- NOTES ---")
        for i, nts in enumerate(notes, 1):
            print(f"{i}. Note: {nts['Note']} | {nts['Date']}")
        print()

    def addNote():
        note = input("Enter the note: ")
        
        notes.append({
            "Note": note,
            "Date": datetime.now().strftime("%d/%m/%Y"),
        })
        saveNotes()

    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = get_number("Choose: ")

        if choice == 1:
            addNote()   
        elif choice == 2:
            viewNotes()
        elif choice == 3:
            break