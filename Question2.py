class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

# Demonstrate usage
account = BankAccount(100)  # Create account with an initial balance of $100

# Deposit money
account.deposit(50)  # Expected to add $50 to the balance
print(f"Current Balance: ${account.get_balance():.2f}")

# Withdraw money
account.withdraw(30)  # Expected to subtract $30 from the balance
print(f"Current Balance: ${account.get_balance():.2f}")

# Try to access balance directly (should not work)
# print(account.__balance)  # This would raise an AttributeError if uncommented
