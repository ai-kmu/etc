class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bits = n & 1
            ans = ans | bits << (31-i)
            n = n >> 1

        return ans
