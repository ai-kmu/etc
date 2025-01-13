# 너무 쉬워서 주석 생략.
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if len(self.balance) >= account1 and len(self.balance) >= account2:
            if self.balance[account1-1] >= money:
                self.balance[account1-1] = self.balance[account1-1] - money
                self.balance[account2-1] = self.balance[account2-1] + money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if len(self.balance) >= account:
            self.balance[account-1] = self.balance[account-1] + money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if len(self.balance) >= account:
            if self.balance[account-1] >= money:
                self.balance[account-1] = self.balance[account-1] - money 
                return True
        return False
        
    

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
