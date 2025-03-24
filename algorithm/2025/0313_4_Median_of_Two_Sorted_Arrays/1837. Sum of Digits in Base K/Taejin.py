import math

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        i = int(math.log(n) / math.log(k))
        digits = []
        while i > 0:
            digits.append(n // k**i)
            n %= (k**i)
            i -= 1

        return sum(digits) + n
