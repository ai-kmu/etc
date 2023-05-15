# Time Limit Exceeded...?
class Solution(object):
    def numSquares(self, n):

        square_list = []
        for i in range(1, int(n ** 0.5) + 1):
            square_list.append(i*i)

        def solve(n):
            if n == 0:
                return 0
            if n < 0:
                return float("inf")
            min_val = n
            for i in square_list:
                min_val = min(min_val, solve(n - i))
            return min_val + 1
        return solve(n)
