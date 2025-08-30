from bank import Bank

def main():
    bank = Bank("MyBank")

    # Create accounts
    bank.create_account("savings", "S001", "Alice", 1000)
    bank.create_account("current", "C001", "Bob", 500)

    # Access accounts
    alice = bank.get_account("S001")
    bob = bank.get_account("C001")

    # Operations
    alice.deposit(200)
    alice.withdraw(100)
    alice.apply_interest()

    bob.deposit(300)
    bob.withdraw(600)  # within overdraft
    # bob.withdraw(2000)  # This will throw overdraft error

    # Transfer money
    bank.transfer("S001", "C001", 250)

    # Account Info
    print(alice.get_account_info())
    print(bob.get_account_info())

if __name__ == "__main__":
    main()
