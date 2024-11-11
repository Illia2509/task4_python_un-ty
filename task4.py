class BankAccount:
    def __init__(self, balance=0):
        if balance < 0: raise ValueError("Initial balance cannot be negative.")
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0: raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0: raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance: raise ValueError("Not enough funds to withdraw.")
        self.balance -= amount
    
    def get_balance(self):
       return self.balance
    
