# 점화식 사용
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        n2 = 2
        n3 = 3
        tmp = 0

        for _ in range(3, n):
            tmp = n2 + n3
            n2 = n3
            n3 = tmp
        return tmp
