import core.config as config
from core.utils import new_window
import time

un = config.username

def calculator():
    new_window(un)
    while True:
        OPERATORS = ["+", "-", "*", "/", "exit"]
        usrOp = input(f"Enter the operator from {OPERATORS} ")

        if usrOp not in OPERATORS:
            print(f"Please chose from {OPERATORS} ")
            continue
        
        elif usrOp == "exit":
            print("Exiting")
            time.sleep(1)
            break

        else:
            num1 = int(input("Enter x (number 1): "))
            num2 = int(input("Enter y (number 2): "))

            if usrOp == "*":
                answer = num1 * num2
                print(f"{num1} * {num2} = {answer}")
            elif usrOp == "/":
                answer = num1 / num2
                print(f"{num1} / {num2} = {answer}")
            elif usrOp == "+":
                answer = num1 + num2
                print(f"{num1} + {num2} = {answer}")
            elif usrOp == "-":
                answer = num1 - num2
                print(f"{num1} - {num2} = {answer}")