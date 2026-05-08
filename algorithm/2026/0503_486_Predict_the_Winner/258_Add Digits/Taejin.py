class Solution:
    def addDigits(self, num: int) -> int:
        if num:
            return num % 9 if num % 9 else 9

        else:
            return num
