import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        
        divisor_sum = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisor_sum += i
                
                if i * i != num:
                    divisor_sum += (num // i)
                    
        return divisor_sum == num
