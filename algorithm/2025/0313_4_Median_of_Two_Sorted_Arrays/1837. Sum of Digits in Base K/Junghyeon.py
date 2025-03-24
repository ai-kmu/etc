class Solution:
    def sumBase(self, n: int, k: int) -> int:

        if n == k:
            return 1

        if k == 10:
            result = 0
            for i in str(n):
                result += int(i)

            return result

        i = 0

        while k**i < n:
            i += 1

        i -= 1

        idx = k**i

        result = []

        while idx > 1:
            a = n // idx
            result.append(a)
            n = n - (idx*a)
            
            print(n)
            
            idx = idx // k
            
        result.append(n)

        return sum(result)
