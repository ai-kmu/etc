class Bank: 

    def __init__(self, balance: List[int]):
        self.balance = balance[::]
        self.length = len(self.balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (account1 > self.length) or (account2 > self.length) or (money > self.balance[account1 - 1]):
            return False

        else:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.length:
            return False

        else:
            self.balance[account - 1] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        if (account > self.length) or (money > self.balance[account - 1]):
            return False
        
        else:
            self.balance[account - 1] -= money
            return True
