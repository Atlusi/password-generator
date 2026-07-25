import json
import os
import random
import string
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def generate_password(config):

    characters = ""

    if config["lowercase"]:
        characters += string.ascii_lowercase

    if config["uppercase"]:
        characters += string.ascii_uppercase

    if config["numbers"]:
        characters += string.digits

    if config["symbols"]:
        characters += string.punctuation

    if characters == "":
        print("No character type selected. Enable at least one setting.")
        return


    try:
        num_chars = int(input("Enter the number of characters for the password: "))
    except ValueError:
        print("Invalid number! Going back to menu.")
        time.sleep(2)
        return

    if num_chars <= 0:
        print("Invalid length! Going back to menu.")
        time.sleep(2)
        return


    try:
        num_pwd = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Invalid number! Going back to menu.")
        time.sleep(2)
        return

    if num_pwd <= 0:
        print("Invalid number! Going back to menu.")
        time.sleep(2)
        return


    passwords = []

    for password_number in range(num_pwd):
        password = ""

        for character in range(num_chars):
            password += random.choice(characters)

        passwords.append(password)

    return passwords



def settings(config):

    while True:

        clear_screen()

        print(f"""
        ========================
                Settings
        ========================
        (Type the number to toggle the setting.)

    1. Lowercase : {"ON" if config["lowercase"] else "OFF"}
    2. Uppercase : {"ON" if config["uppercase"] else "OFF"}
    3. Numbers   : {"ON" if config["numbers"] else "OFF"}
    4. Symbols   : {"ON" if config["symbols"] else "OFF"}

    5. Back
    """)

        choice = input("> ")

        if choice == "1":
            config["lowercase"] = not config["lowercase"]


        elif choice == "2":
            config["uppercase"] = not config["uppercase"]


        elif choice == "3":
            config["numbers"] = not config["numbers"]


        elif choice == "4":
            config["symbols"] = not config["symbols"]


        elif choice == "5":
            break
        
        else:
            print("Invalid choice")



def load_history():

    history_path = "history.json"

    if os.path.exists(history_path) and os.path.isfile(history_path):
        with open(history_path, "r") as f:
            history = json.load(f)
            return history
    else:
        history = []
        return history



def save_history(history):
    with open("history.json", "w") as f:
        json.dump(history, f, indent= 4)    



def show_history(history):
        
        clear_screen()

        print("""
        ========== History ==========
        """)

        if not history:
            print("""
        No password generated yet.
                """)
            input("\nPress Enter to go back to the menu...")
            return
        
        for number, item in enumerate(history, 1):
            print(f"""
#{number}
Password: {item["password"]}
Comment: {item["comment"]}
-----------------------------
""")
        input("\nPress Enter to go back to the menu...")


def main():

    history = load_history()
    
    config = {
        "lowercase": True,
        "uppercase": True,
        "numbers": True,
        "symbols": True
    }


    while True:

        clear_screen()

        print("""
        ============================================
                 Password Generator v1.0
        ============================================
        1. Generate Password
        2. Settings
        3. History
        4. Exit
        """)

        choice = input("> ")

        if choice == "1":

            passwords = generate_password(config)

            if passwords is None:
                continue

            for number, pwd in enumerate(passwords, 1):
                print(f"\nPassword #{number}: {pwd}")

                comment = input("Add a comment (password to what?): ")

                history.append({
                    "password": pwd,
                    "comment": comment
                })

                save_history(history)

        elif choice == "2":
            settings(config)

        elif choice == "3":
            show_history(history)

        elif choice == "4":
            clear_screen()
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()