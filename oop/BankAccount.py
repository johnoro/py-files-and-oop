class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def bank_fee(self):
        self.balance -= self.balance * 0.05
    def display(self):
        print("Account Number: ", self.account_number)
        print("Name: ", self.name)
        print("Balance: ", self.balance)
