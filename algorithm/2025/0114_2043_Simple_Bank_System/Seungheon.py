class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.money = balance

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """

        try:
            account1 -= 1
            account2 -= 1
            if self.money[account1] >=  money and self.money[account2] is not None: 
                self.money[account1] -= money
                self.money[account2] += money
                return True
            else:
                return False
        except:
            return False
        

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        try:
            account -= 1
            self.money[account] += money
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
            account -= 1
            if self.money[account] >=  money:
                self.money[account] -= money
                return True
            else:
                return False
        except:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
