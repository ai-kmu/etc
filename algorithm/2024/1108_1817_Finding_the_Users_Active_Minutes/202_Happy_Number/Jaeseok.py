class Solution:
    def isHappy(self, n: int) -> bool:
        number = 0
        n = str(n)
        while True:
            for d in str(n):
                number += int(d) ** 2
            n = number
            if number < 7 and number != 1:
                return False
            if number == 1:
                return True
            number = 0
            
