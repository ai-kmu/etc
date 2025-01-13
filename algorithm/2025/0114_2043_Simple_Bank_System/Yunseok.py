from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, from_acc: int, to_acc: int, money: int) -> bool:
        # 유효성 검증
        if not (1 <= from_acc <= len(self.balance) and 1 <= to_acc <= len(self.balance)):
            return False
        # 잔고 확인
        if self.balance[from_acc - 1] < money:
            return False
        # 송금
        self.balance[from_acc - 1] -= money
        self.balance[to_acc - 1] += money
        return True

    def deposit(self, acc: int, money: int) -> bool:
        # 유효성 검증
        if not (1 <= acc <= len(self.balance)):
            return False
        # 입금
        self.balance[acc - 1] += money
        return True

    def withdraw(self, acc: int, money: int) -> bool:
        # 유효성 검증 & 잔고 확인
        if not (1 <= acc <= len(self.balance)) or self.balance[acc - 1] < money:
            return False
        # 인출
        self.balance[acc - 1] -= money
        return True
