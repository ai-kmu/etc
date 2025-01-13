class Bank:

    def __init__(self, balance: List[int]):
        # 초기 계좌 잔액을 나타내는 리스트를 저장
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # 두 계좌 번호가 유효하고 출금 계좌에 충분한 잔액이 있는 경우 송금을 진행
        if self._is_valid_account(account1) and self._is_valid_account(account2):
            if self.balance[account1 - 1] >= money:
                # 송금 계좌에서 금액 차감
                self.balance[account1 - 1] -= money
                # 입금 계좌에 금액 추가
                self.balance[account2 - 1] += money
                return True
        # 조건을 충족하지 못하면 False 반환
        return False

    def deposit(self, account: int, money: int) -> bool:
        # 계좌 번호가 유효한 경우 지정된 계좌에 입금을 진행
        if self._is_valid_account(account):
            # 계좌에 금액 추가
            self.balance[account - 1] += money
            return True
        # 유효하지 않은 계좌일 경우 False 반환
        return False

    def withdraw(self, account: int, money: int) -> bool:
        # 계좌 번호가 유효하고 잔액이 충분한 경우 출금
        if self._is_valid_account(account):
            if self.balance[account - 1] >= money:
                # 계좌에서 금액 차감
                self.balance[account - 1] -= money
                return True
        # 조건을 충족하지 못하면 False 반환
        return False

    def _is_valid_account(self, account: int) -> bool:
        # 계좌 번호가 1 이상이고 총 계좌 수 이하인지 확인
        return 1 <= account <= len(self.balance)
