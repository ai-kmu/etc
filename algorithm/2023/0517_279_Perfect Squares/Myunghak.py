class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)][::-1]
        squares_set = set(squares)

        def dp(n, ans, squares, min_ans):
            if n in squares_set:
                min_ans = min(min_ans, ans + 1)
                return min_ans

            for i, s in enumerate(squares):
                if ans+1 > min_ans:
                    break
                elif n - s >= 0:
                    min_ans = dp(n - s, ans + 1, squares[i:], min_ans)

            return min_ans
        
        return dp(n, 0, squares, n)
