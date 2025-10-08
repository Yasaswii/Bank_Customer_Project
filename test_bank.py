from savings_account import SavingsAccount
from bussiness_account import BusinessAccount

def savings_menu(account):
    while True:
        print(" Savings Account Menu")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Request ATM Card")
        print("5. Request Cheque Book")
        print("6. Freeze Account")
        print("7. Unfreeze Account")
        print("8. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            pin = int(input("Enter PIN: "))
            account.check_balance(pin)
        elif choice == "2":
            pin = int(input("Enter PIN: "))
            amount = float(input("Enter amount to deposit: "))
            account.deposit(pin, amount)
        elif choice == "3":
            pin = int(input("Enter PIN: "))
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(pin, amount)
        elif choice == "4":
            account.request_atm_card()
        elif choice == "5":
            account.request_cheque_book()
        elif choice == "6":
            account.freeze_account()
        elif choice == "7":
            account.unfreeze_account()
        elif choice == "8":
            break
        else:
            print("Invalid choice, try again.")


def business_menu(account):
    while True:
        print("Business Account Menu")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Request Cheque Book")
        print("5. Freeze Account")
        print("6. Unfreeze Account")
        print("7. Exit to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "4":
            account.request_cheque_book()
        elif choice == "5":
            account.freeze_account()
        elif choice == "6":
            account.unfreeze_account()
        elif choice == "7":
            break
        else:
            print("Invalid choice, try again.")



while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Savings Account")
    print("2. Business Account")
    print("3. Exit")
    account_choice = input("Enter your choice: ")

    if account_choice == "1":
        name = input("Enter your name: ")
        balance = float(input("Enter initial balance: "))
        pin = int(input("Set 4-digit PIN: "))
        s_acc = SavingsAccount(name, balance, pin)
        savings_menu(s_acc)

    elif account_choice == "2":
        bname = input("Enter business name: ")
        balance = float(input("Enter initial balance: "))
        b_acc = BusinessAccount(bname, balance)
        business_menu(b_acc)

    elif account_choice == "3":
        print("Thank you for using the bank system.")
        break
    else:
        print("Invalid choice, try again.")