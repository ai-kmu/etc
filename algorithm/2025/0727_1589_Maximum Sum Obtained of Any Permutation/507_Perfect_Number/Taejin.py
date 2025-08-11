class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        factors = set([1])

        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)

        return (num != 1) and (sum(factors) == num)

        
