class Bank:

    def __init__(self, balance: List[int]):
        self.length = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 - 1 > self.length or account2 - 1 > self.length or account1 - 1 < 0 or account2 - 1 < 0:
            return False

        if self.balance[account1-1] >= money:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account - 1 > self.length or account - 1 < 0:
            return False
        else:
            self.balance[account-1] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        if account - 1 > self.length or account - 1 < 0:
            return False
        else:
            if self.balance[account-1] < money:
                return False
            else:
                self.balance[account-1] -= money
                return True
