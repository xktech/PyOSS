from .expenseTracker import expenseTracker
from .homework import homeworkList

def render_school():
    print("-" * 38)
    print("1. Expenses Tracker")
    print("2. Homework List")
    print("3. Back")
    print("")


def school_menu():
    while True:
        render_school()

        schoolChoice = input(">> ").lower().strip()

        if schoolChoice == "expenses tracker":
            expenseTracker()
        elif schoolChoice == "homework list":
            homeworkList()
        elif schoolChoice == "back":
            break
        else:
            print("Unknown Command")