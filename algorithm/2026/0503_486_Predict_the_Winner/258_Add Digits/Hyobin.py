class Solution:
    def addDigits(self, num: int) -> int:
        while(num // 10 >= 1):
            num = (num // 10) + (num % 10)

        return num

# ====================================

class Solution:
    def addDigits(self, num: int) -> int:
        if num % 9 == 0 and num != 0:
            return 9
        else:
            return num % 9
