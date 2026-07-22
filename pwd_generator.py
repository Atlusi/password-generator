import random
import time 
import string

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


    pwds = []

    for password_number in range(num_pwd):
        password = ""

        for character in range(num_chars):
            password += random.choice(characters)

        pwds.append(password)

    return pwds


def settings(config):

    while True:
        print("""
        ========================
               Settings
        ========================
        (Type the number to change the setting.)

        1. Lowercase
        2. Uppercase
        3. Numbers
        4. Symbols
        5. Back
        """)

        print(config)

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


def main():

    config = {
        "lowercase": True,
        "uppercase": True,
        "numbers": True,
        "symbols": True
    }

    while True:

        print("""
        ============================================
                    Password Generator
        ============================================
        1. Generate Password
        2. Settings
        3. Exit
        """)

        choice = input("> ")

        if choice == "1":

            passwords = generate_password(config)
            print("\nGenerated Passwords:")
            for pwd in passwords:
                print(pwd)

            print()

        elif choice == "2":
            settings(config)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()

# Problème : faire qu'on doit avoir au moins 1 setting activé. -> Afficher "Error: Need to have at least 1 setting active!" quand ça detecte que 
# ça veut désac le dernier true
# Use raise ? Perhaps. 


