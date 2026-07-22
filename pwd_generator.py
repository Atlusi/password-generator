import random
import time 
def generate_password():
    num_chars = int(input("Enter the number of characters for the password: "))

    if num_chars <= 0:
            print("Invalid length! Going back to menu.")
            time.sleep(2)
            main()
    
    num_pwd = int(input("Enter the number of passwords to generate: "))
 
    if num_pwd <= 0:
        print("Invalid length! Going back to menu.")
        time.sleep(2)
        main()            
    
    pwds = []
    for j in range(num_pwd):
        password = ""
        for j in range(num_chars):
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+,.()[]{}%£$")
        pwds.append(password)  

    return pwds


def main():
    while True:
        print("""
        ============================================
                    Password Generator
        ============================================
        1. Generate Password
        2. Exit 
        """)

        choice = input("> ")

        if choice == "1":
            passwords = generate_password()
            print("\nGenerated Passwords :")
            for pwd in passwords:
                print(pwd)
            print()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")


#######
if __name__ == "__main__":

    main()

# note to ms : faire try/except pour ValueError (Error handling)
# Faire fonctionnalité ajouter customiser le password : include lowercase, uppercase, numbers, symbols....

