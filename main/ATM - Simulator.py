import json
import os



def create_account(count):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return
    balance = float(input("Enter your initial balance: "))

    os.makedirs("src/data", exist_ok=True)

    accounts_path = "src/data/accounts.json"
    if os.path.exists(accounts_path):
        with open(accounts_path, "r", encoding="utf-8") as file:
            accounts = json.load(file)
    else:
        accounts = {}
    

    accounts[str(count)] = { "name": name, "password": password, "balance": balance} 



    with open("src/data/accounts.json",  "w", encoding="utf-8") as file:
            file.write(json.dumps(accounts, indent=4))
    print(f"Account created successfully! Your account number is {count}.")
    return 1   
    
def mainController():
    print("Please select an option:\n 1. Create Account\n 2. Login\n 0. Exit")
    num = int(input("Enter your choice: "))
    return num
    

print("WELCOME TO ATM SIMULATOR")
isProgramRunning = True
count = 1
while isProgramRunning:
    num = mainController()
    if num == 1:
        count = count + create_account(count)

    elif num == 2:
        print("soon")
    elif num == 0:
        print("Exiting the ATM Simulator. Goodbye!")
        isProgramRunning = False
    else:
        print("Invalid option. Please try again.")



