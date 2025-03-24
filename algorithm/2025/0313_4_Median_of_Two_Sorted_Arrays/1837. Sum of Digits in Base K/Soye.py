class Solution:
    def sumBase(self, n: int, k: int) -> int:
        tmp = ''

        while n:
            tmp += str(n%k)
            n = n//k

        tmp = tmp[::-1]
        ans = 0

        for idx in tmp:
            ans += int(idx)

        return ans
