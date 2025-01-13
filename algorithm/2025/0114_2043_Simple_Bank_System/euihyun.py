
class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.bank = balance
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        try:
            #유효한지
            if account1 < 1 or account1 > len(self.bank) or account2 < 1 or account2 > len(self.bank):
                return False            
            # 돈 전송하고 유효한지
            self.bank[account1-1] -=  money
            if self.bank[account1-1] >= 0:
                self.bank[account2-1] +=  money
                return True
            # 안되면 돌려줘
            else:
                self.bank[account1-1] +=  money
                return False
        except:
            return False

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # 돈 넣어~ 리스트 나가면 어차피 excpet됨
        try:
            self.bank[account-1] += money
            return True
        except:
            return False
    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        try:
            # 돈빼
            self.bank[account-1] -= money
            # 유효하면 되고 안되면 False
            if self.bank[account-1] >= 0 :
                return True            
            else:
                self.bank[account-1] += money
                return False            
        except:
            return False



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

