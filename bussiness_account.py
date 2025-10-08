class BusinessAccount:
    def __init__(self, business_name, balance):
        self.business_name = business_name
        self.balance = balance
        self.active = True
        self.cheque_requested = False

    def check_balance(self):
        if not self.active:
            print("Account is inactive.")
        else:
            print("Business Balance:", self.balance)

    def withdraw(self, amount):
        if not self.active:
            print("Account is frozen.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print("Withdrawal successful. Remaining balance:", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print("Deposit successful. Updated balance:", self.balance)

    def request_cheque_book(self):
        if self.cheque_requested:
            print("Cheque book already requested.")
        else:
            self.cheque_requested = True
            print("Cheque book request approved.")

    def freeze_account(self):
        if not self.active:
            print("Account already frozen.")
        else:
            self.active = False
            print("Account frozen successfully.")

    def unfreeze_account(self):
        if self.active:
            print("Account already active.")
        else:
            self.active = True
            print("Account unfrozen successfully.")