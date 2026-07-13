import os
import json
import datetime
from core.utils import get_number

def homeworkList(): # Added from Student Dashboard

    HOMEWORK_FILE = "homework.json"

    def loadHomework():
        if os.path.exists(HOMEWORK_FILE):
            with open(HOMEWORK_FILE, "r") as f:
                return json.load(f)
        return []
    homework = loadHomework() 

    def getValidDate(prompt):
        while True:
            date_str = input(prompt)
            try:
                datetime.strptime(date_str, "%d/%m/%Y")
                return date_str
            except ValueError:
                print("Invalid date! Please use: DD/MM/YYYY format (e.g. 28/04/2026)")

    def saveHomework():
        with open(HOMEWORK_FILE, "w") as f:
            json.dump(homework, f, indent=2)
    def addHomework():
        subject = input("Enter the subject: ")
        teacher = input("Enter the teacher: ")
        task = input("Enter your homework task: ")
        due_date = getValidDate("Enter due date (DD/MM/YYYY): ")

        homework.append({
            "Subject": subject,
            "Teacher": teacher,
            "Task": task,
            "Due": due_date,
            "Date": datetime.now().strftime("%d/%m/%Y")
        })
        saveHomework()
    def viewHomework():
        def viewHomework():
            if not homework:
                print("No homework saved!")
                return

        print("\n--- Homework List ---")
        for i, hw in enumerate(homework, 1):
            print(f"{i}. [{hw['Subject']}] {hw['Task']} - {hw['Teacher']} | Due: {hw['Due']} {hw['Date']}")
        print()

    while True:
        print("\n1. Add Homework:")
        print("2. View Homework")
        print("3. Exit")

        choice = get_number("Choose: ")

        if choice == 1:
            addHomework()
        if choice == 2:
            viewHomework()
        if choice == 3:
            break