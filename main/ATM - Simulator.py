import json
import os
import random

def create_account(count, accounts_path):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        return 0
    balance = float(input("Enter your initial balance: "))

    os.makedirs("src/data", exist_ok=True)

    

    if os.path.exists(accounts_path):
        with open(accounts_path, "r", encoding="utf-8") as file:
            try:
                accounts = json.load(file)
            except json.JSONDecodeError:
                print("Error reading accounts file. It may be corrupted.")
                accounts = {}
                return 0
    else:
        accounts = {}
    

    accounts[str(count + random.randint(1,1000))] = { "name": name, "password": password, "balance": balance , "transactions": [""] } 



    with open(accounts_path,  "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4, ensure_ascii=False)

    print(f"Account created successfully! Your account number is {accounts.keys}.")
    return 1   
    
def mainController():
    print("Please select an option:\n 1. Create Account\n 2. Login\n 0. Exit")
    return int(input("Enter your choice: "))

def check_balance(accout):
    print("Your current balance is: ", accout["balance"])    

def deposit(account):
    value = float(input("Enter the amount to desposit: "))
    if value <= 0:
        print("Deposit amount must be greater than zero.")
        return
    account["balance"] += value
    account["transactions"].append(f"Deposited: {value}")
    print(f"You have successfully deposited {value} into your account.")


def withdraw(account):
    value = float(input("Enter the amount to withdraw: "))
    if value <= 0:
        print("Withdrawal amount must be greater than zero.")
        return
    if value > account["balance"]:
        print("Insufficient balance for this withdrawal.")
        return
    account["balance"] -= value
    account["transactions"].append(f"Withdrew: {value}")
    print(f"You have successfully withdrawn {value} from your account.")

def view_transactions(account):
    print("Your transactions:")
    if not account["transactions"]:
        print("No transactions found.")
    else:
        for transaction in account["transactions"]:
            print(transaction)

def logout():
    print("You have been logged out.\n")
    return False

def verify_password(account, password):
    if account["password"] == password:
        return True
    else:
        print("Incorrect password.")
        return False    

def management_controller(isLoggedIn, accounts):
    while isLoggedIn:
        print("\nPlease select an option:\n 1. Check Balance\n 2. Deposit\n 3. Withdraw\n 4. View Transactions\n 5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            view_transactions(accounts)
        elif choice == "5":
            isLoggedIn = logout()
        else:
            print("Invalid option. Please try again.")

def login(accounts_path):
    with open(accounts_path, "r", encoding="utf-8") as file:
        accounts = json.load(file)

    for i in range  (accounts.__len__()):
        print(f"Account {i + 1}: {accounts[str(i + 1)]['name']}")


    account_number = input("Enter your account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return
    
    password = input("Enter your password: ")

    if not verify_password(accounts[account_number], password):
        return
    
    print(f"Welcome {accounts[account_number]['name']}!")
    isLoggedIn = True
    management_controller(isLoggedIn, accounts[account_number])





print("WELCOME TO ATM SIMULATOR")
isProgramRunning = True
count = 1
accounts_path = "src/data/accounts.json"
while isProgramRunning:
    num = mainController()
    if num == 1:
        print("Creating a new account...")
        count = count + create_account(count, accounts_path)

    elif num == 2:
        print("Logging in...")
        login(accounts_path)
        
    elif num == 0:
        print("Exiting the ATM Simulator. Goodbye!")
        isProgramRunning = False
    else:
        print("Invalid option. Please try again.")



