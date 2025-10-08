class SavingsAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.active = True
        self.card_requested = False
        self.cheque_requested = False
        self.daily_limit = 10000

    def check_balance(self, pin):
        if not self.active:
            print("Account is inactive.")
        elif pin != self.pin:
            print("Incorrect PIN.")
        else:
            print("Balance:", self.balance)

    def withdraw(self, pin, amount):
        if pin != self.pin:
            print("Incorrect PIN.")
        elif not self.active:
            print("Account is frozen.")
        elif amount > self.balance:
            print("Insufficient funds.")
        elif amount > self.daily_limit:
            print("Exceeds daily withdrawal limit.")
        else:
            self.balance -= amount
            print("Withdrawal successful. Remaining balance:", self.balance)

    def deposit(self, pin, amount):
        if pin != self.pin:
            print("Incorrect PIN.")
        elif amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print("Deposit successful. Updated balance:", self.balance)

    def request_atm_card(self):
        if self.card_requested:
            print("ATM card already requested.")
        else:
            self.card_requested = True
            print("ATM card request approved.")

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

