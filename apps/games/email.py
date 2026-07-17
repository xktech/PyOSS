import core.config as config
from core.utils import get_number
from core.utils import new_window
import time



day1_schedule = [
    (0, "Welcome"),
    (10, "HR"),
    (20, "Printer Not Working"),
    (30, "Password Reset"),
    (40, "Coffee Machine"),
    (60, "Unknown Sender")
]
day1_emails = {
    "Welcome":
"""Welcome to Blackwood Systems!

We are very excited to have you join our overnight IT department.

Your responsibilities include:
- Responding to staff emails
- Resetting passwords
- Assisting with technical issues

Have a great first shift!
""",

    "HR":
"""Hi!

Just a reminder to complete your employee paperwork by the end of the week.

Thanks,
Human Resources
""",

    "Printer Not Working":
"""Hello IT,

The printer on Floor 2 isn't printing anything. It just flashes a red light.

Could you have a look when you get a chance?

Thanks,
Sarah
""",

    "Password Reset":
"""Hi,

(USER) has requested a password reset.

If this request wasn't made by the user, please ignore this email.

Regards,
Automated IT System
""",

    "Coffee Machine":
"""Morning,

The coffee machine in the staff kitchen keeps displaying 'ERROR 14'.

Can someone from IT check it? Nobody can survive the night shift without coffee.

Thanks,
Dave
""",

    "Unknown Sender":
"""Hello?

Someone answered.

"""
}

def play():
    start_time = time.time()
    inbox = []
    delivered = set()
    while True:
        elapsed = int(time.time() - start_time)

        for arrival_time, subject in day1_schedule:
            if elapsed >= arrival_time and subject not in delivered:
                delivered.add(subject)
                inbox.append(subject)

                print(f"New Email: {subject}")
        
        command = input("> ")

        if command.lower() == "mail":
            print("\n Inbox")
            for i, subject in enumerate(inbox, 1):
                print(f"{i}. {subject}")

        elif command.isdigit():
            index = int(command) - 1
            if 0 <= index <len(inbox):
                subject = inbox[index]
                print(day1_emails[subject])
def advance():
    pass


def menu():
    while True:
        print("-"*38)
        print("1. Start")
        print("2. Advance to next day")
        print("3. EXIT")
        print("-"*38)

        choice = get_number("> ")

        if choice == 1:
            play()
        elif choice == 2:
            advance()
        elif choice == 3:
            break
if __name__ == "__main__":
    menu()