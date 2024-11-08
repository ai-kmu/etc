class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        
        while n not in numbers:
            numbers.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
            
        
        return n == 1
