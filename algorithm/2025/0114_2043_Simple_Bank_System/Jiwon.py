class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.len = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # account1에서 money가 출금 가능한 경우
        if self.withdraw(account1, money):
            # account2로 입금 가능할 경우
            if self.deposit(account2, money):
                return True
            # account2에 입금 불가능한 경우 다시 반환
            self.deposit(account1, money)
        return False

    def deposit(self, account: int, money: int) -> bool:
        # 유효한 거래 판단 1 (계좌번호)
        if 1 <= account <= self.len:
            self.balance[account - 1] += money
            return True 
        return False

    def withdraw(self, account: int, money: int) -> bool:
        # 유효한 거래 판단 1 (계좌번호)
        if 1 <= account <= self.len:
            # 유효한 거래 판단 2 (잔액)
            if self.balance[account - 1] >= money:
                self.balance[account - 1] -= money
                return True 
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
