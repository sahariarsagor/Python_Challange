import random
import os

FILE_NAME = "bank_data.txt"
BANK_PREFIX = "SB"


# ---------------- Utility Functions ----------------

def generate_account_number():
    return BANK_PREFIX + str(random.randint(10000000, 99999999))


def load_all_accounts():
    accounts = []

    if not os.path.exists(FILE_NAME):
        return accounts

    with open(FILE_NAME, "r") as file:
        for line in file:
            acc_no, name, pin, balance = line.strip().split("|")
            accounts.append({
                "account_no": acc_no,
                "name": name,
                "pin": pin,
                "balance": float(balance)
            })

    return accounts


def save_all_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        for acc in accounts:
            file.write(
                f"{acc['account_no']}|{acc['name']}|{acc['pin']}|{acc['balance']}\n"
            )


# ---------------- Core Functions ----------------

def create_account():
    accounts = load_all_accounts()

    name = input("Enter your name: ")
    pin = input("Set a 4-digit PIN: ")
    balance = float(input("Enter initial balance: "))

    account_no = generate_account_number()

    new_account = {
        "account_no": account_no,
        "name": name,
        "pin": pin,
        "balance": balance
    }

    accounts.append(new_account)
    save_all_accounts(accounts)

    print("\n✅ Account created successfully!")
    print("Account Number:", account_no)


def login():
    accounts = load_all_accounts()

    if not accounts:
        print("\n❌ No accounts found. Please create one first.")
        return None, None

    acc_no = input("Enter Account Number: ")
    pin = input("Enter PIN: ")

    for acc in accounts:
        if acc["account_no"] == acc_no and acc["pin"] == pin:
            print("\n🔓 Login successful!")
            return acc, accounts

    print("\n❌ Invalid Account Number or PIN!")
    return None, None


def deposit(account, accounts):
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("❌ Invalid amount!")
        return

    account["balance"] += amount
    save_all_accounts(accounts)

    print("✅ Deposit successful!")
    print("Current Balance:", account["balance"])


def withdraw(account, accounts):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("❌ Invalid amount!")
        return

    if amount > account["balance"]:
        print("❌ Insufficient balance!")
        return

    account["balance"] -= amount
    save_all_accounts(accounts)

    print("✅ Withdrawal successful!")
    print("Current Balance:", account["balance"])


def check_balance(account):
    print("\n💰 Current Balance:", account["balance"])


# ---------------- Menus ----------------

def banking_menu(account, accounts):
    while True:
        print("\n==============================")
        print(f"Welcome, {account['name']}")
        print(f"Account Number: {account['account_no']}")
        print("==============================")

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            deposit(account, accounts)
        elif choice == "2":
            withdraw(account, accounts)
        elif choice == "3":
            check_balance(account)
        elif choice == "4":
            print("👋 Logged out successfully.")
            break
        else:
            print("❌ Invalid choice!")


def main_menu():
    while True:
        print("\n=== Sahariar Bank ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            account, accounts = login()
            if account:
                banking_menu(account, accounts)
        elif choice == "3":
            print("\n🙏 Thank you for using Sahariar Bank!")
            break
        else:
            print("❌ Invalid choice!")


# ---------------- Program Start ----------------
main_menu()
