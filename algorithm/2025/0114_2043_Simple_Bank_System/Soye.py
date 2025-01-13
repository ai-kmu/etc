class Bank:

    def __init__(self, balance: List[int]):
        self.bankAccounts = balance  # 각 계좌의 잔고 저장
        self.length = len(self.bankAccounts)  # 계좌의 총 개수 저장

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # 계좌 간 송금 메서드
        if 1 <= account1 <= self.length and 1 <= account2 <= self.length:  # 계좌 번호가 유효한지 확인
            if money <= self.bankAccounts[account1 - 1]:  # 송금 계좌에 충분한 잔고가 있는지 확인
                self.bankAccounts[account1 - 1] -= money  # 송금 계좌에서 금액 차감
                self.bankAccounts[account2 - 1] += money  # 수신 계좌에 금액 추가
                return True  # 송금 성공
        return False  # 송금 실패

    def deposit(self, account: int, money: int) -> bool:
        # 입금 메서드
        if 1 <= account <= self.length:  # 계좌 번호가 유효한지 확인
            self.bankAccounts[account - 1] += money  # 해당 계좌에 금액 추가
            return True  # 입금 성공
        return False  # 입금 실패

    def withdraw(self, account: int, money: int) -> bool:
        # 출금 메서드
        if 1 <= account <= self.length:  # 계좌 번호가 유효한지 확인
            if money <= self.bankAccounts[account - 1]:  # 계좌 잔고가 충분한지 확인
                self.bankAccounts[account - 1] -= money  # 계좌에서 금액 차감
                return True  # 출금 성공
        return False  # 출금 실패


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
