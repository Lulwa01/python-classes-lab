class BankAccount():
    def __init__(self, owner, balance, account_no=0, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.account_no = account_no
        self.has_overdraft = has_overdraft

    def depsit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.has_overdraft:
            self.balance -= amount
            if amount > self.balance:
                return "withdraw denied"
            else:
                self.balance -= amount
                return self.balance
    
    def __str__(self):
        return f"Account: {self.account_no} - Balance: {self.balance}"