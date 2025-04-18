import random

class BankAccount():
    def __init__(self, owner, balance, account_no=0, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.has_overdraft = has_overdraft

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.has_overdraft and amount <= self.balance:
            return "withdraw denied"
        else:
            self.balance -= amount
            return self.balance
        
    def __str__(self):
        return f"Account: {self.account_no} - Balance: {self.balance}"
    
class SavingsAccount(BankAccount): 
    def __init__(self, owner, balance, account_no=0, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.has_overdraft = has_overdraft
        
    def withdraw(self):
        return "No withdrawals permitted"