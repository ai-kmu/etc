class Bank:
    # index check는 try-except로 구현
    # 금액 check는 if문으로 구현
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        try:
            if self.balance[account1-1] < money:
                return False
            self.balance[account2-1] += money
        except IndexError:
            return False
        self.balance[account1-1] -= money
        return True

    def deposit(self, account: int, money: int) -> bool:
        try:
            self.balance[account-1] += money
        except IndexError:
            return False
        return True

    def withdraw(self, account: int, money: int) -> bool:
        try:
            if self.balance[account-1] < money:
                return False
        except IndexError:
            return False
        self.balance[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
