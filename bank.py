from abc import ABC, abstractmethod

# Abstract Class
class BankAccount(ABC):
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number  # Encapsulation (protected)
        self._owner = owner
        self._balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        print(f"{amount} deposited. New balance: {self._balance}")

    def get_balance(self):
        return self._balance

    def get_account_info(self):
        return f"Account[{self._account_number}] - Owner: {self._owner}, Balance: {self._balance}"


# Inheritance + Polymorphism
class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds in Savings Account")
        self._balance -= amount
        print(f"{amount} withdrawn. Remaining balance: {self._balance}")

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Interest applied: {interest}. New balance: {self._balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded in Current Account")
        self._balance -= amount
        print(f"{amount} withdrawn. Remaining balance: {self._balance}")


# Bank Class to Manage Accounts
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_type, account_number, owner, balance=0):
        if account_type == "savings":
            account = SavingsAccount(account_number, owner, balance)
        elif account_type == "current":
            account = CurrentAccount(account_number, owner, balance)
        else:
            raise ValueError("Invalid account type")

        self.accounts[account_number] = account
        print(f"{account_type.capitalize()} account created for {owner}")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if not sender or not receiver:
            raise ValueError("Invalid account number")

        sender.withdraw(amount)
        receiver.deposit(amount)
        print(f"Transferred {amount} from {from_acc} to {to_acc}")
