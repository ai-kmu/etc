class Bank:

    def __init__(self, balance: List[int]):
        # 계좌 정보 저장
        self.accounts = {i: bal for i, bal in enumerate(balance, 1)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # account1, 2가 있어야 함
        if account1 in self.accounts and account2 in self.accounts:
            # account1에 충분한 돈이 있어야 함
            if self.accounts[account1] >= money:
                self.accounts[account1] -= money  # account1에서 빼서
                self.accounts[account2] += money  # account2에 넣기
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        # account가 있어야 함
        if account in self.accounts:
            self.accounts[account] += money  # account에 넣기
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        # account가 있어야 함
        if account in self.accounts:
            # account에 충분한 돈이 있어야 함
            if self.accounts[account] >= money:
                self.accounts[account] -= money  # account에서 빼기
                return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
