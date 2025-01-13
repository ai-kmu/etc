
# 아래 코드 간단하게 바꾼 버전. 데코레이터 사용(공부하려면 이거 리뷰하는게 좋을듯)

# 데코레이터 생성, try except으로 false 처리
def operation_func(func):
    def wrapper(*args):
        try:
            return func(*args)
        except :
            return False
    return wrapper

class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.money = balance

    @operation_func
    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        account1 -= 1
        account2 -= 1
        if self.money[account1] >= money and self.money[account2] is not None:
            self.money[account1] -= money
            self.money[account2] += money
            return True
        else:
            return False

    @operation_func
    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        account -= 1
        self.money[account] += money
        return True

    @operation_func
    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        account -= 1
        if self.money[account] >= money:
            self.money[account] -= money
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)



# class Bank(object):

#     def __init__(self, balance):
#         """
#         :type balance: List[int]
#         """
#         self.money = balance

#     def transfer(self, account1, account2, money):
#         """
#         :type account1: int
#         :type account2: int
#         :type money: int
#         :rtype: bool
#         """

#         try:
#             account1 -= 1
#             account2 -= 1
#             if self.money[account1] >=  money and self.money[account2] is not None: 
#                 self.money[account1] -= money
#                 self.money[account2] += money
#                 return True
#             else:
#                 return False
#         except:
#             return False
        

#     def deposit(self, account, money):
#         """
#         :type account: int
#         :type money: int
#         :rtype: bool
#         """
#         try:
#             account -= 1
#             self.money[account] += money
#             return True
#         except:
#             return False
        
#     def withdraw(self, account, money):
#         """
#         :type account: int
#         :type money: int
#         :rtype: bool
#         """
#         try:
#             account -= 1
#             if self.money[account] >=  money:
#                 self.money[account] -= money
#                 return True
#             else:
#                 return False
#         except:
#             return False


