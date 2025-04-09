class BankAccount:

    def __init__(self, account_number, account_holder_name, balance = 0.0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount {} withdrawn. New balance is {}".format(amount, self.balance))
        else:
            print("Withdrawal not possible. Account has insufficient balance.")

    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    
    minimum_balance = 500

    def __init__(self, account_number, account_holder_name, balance):
        if balance < SavingsAccount.minimum_balance:
            raise ValueError("Account cannot be created as balance is under minimum balance limit")
        else:
            super().__init__(account_number, account_holder_name, balance)
        
    def withdraw(self, amount):
        if self.balance - amount >= SavingsAccount.minimum_balance:
            return super().withdraw(amount)
        else:
            print("This withdrawal cannot be performed as it breaches minimum balance policy")

class CurrentAccount(BankAccount):

    overdraft_limit = 1000

    def __init__(self, account_number, account_holder_name, balance):
        super().__init__(account_number, account_holder_name, balance)
        self.overdraft_used = 0

    def withdraw(self, amount):
        available_funds = self.balance + CurrentAccount.overdraft_limit - self.overdraft_used
        if amount <= available_funds:
            self.overdraft_used += max(0, amount - self.balance)
            return super().withdraw(amount)
        else:
            print("This withdrawal cannot be performed as it exceeds the overdraft limit.")

def main():
    # Create a savings account
    savings = SavingsAccount("12345", "Alice", 1000)
    savings.withdraw(600)  # Should work
    savings.withdraw(500)  # Should not work (balance can't go below 500)

    # Create a current account
    current = CurrentAccount("67890", "Bob", 500)
    current.withdraw(1200)  # Should work (due to overdraft limit)
    current.withdraw(500)   # Should not work (over limit)

if __name__ == "__main__":
    main()
