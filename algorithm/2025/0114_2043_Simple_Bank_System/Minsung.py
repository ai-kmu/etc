class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.len = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.valid_account(account1) or not self.valid_account(account2) or not self.valid_withdraw(account1, money):
            return False 
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True
        
    def deposit(self, account: int, money: int) -> bool:
        if not self.valid_account(account):
            return False 
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.valid_account(account) or not self.valid_withdraw(account, money):
            return False 
        self.balance[account-1] -= money
        return True
    
    def valid_account(self, account):
        # 유효한 계좌인지 확인
        return False if account<1 or account>self.len else True
    
    def valid_withdraw(self, account, money):
        # 해당 계좌에서 주어진 돈을 인출할 수 있는지 확인
        return True if self.balance[account-1] >= money else False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
