class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 0
        n2 = 1
        tmp = 0

        for _ in range(n):
            tmp = n1 + n2
            n1 = n2
            n2 = tmp

        return n2
