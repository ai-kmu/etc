'''
답지 봤읍이다.
'''

class Solution:
    def findPaths(self, m: int, n: int, max_move: int, start_row: int, start_col: int) -> int:
        memo = {}
        mod = 1000000007

        def solve(x: int, y: int, move: int) -> int:
            if move > max_move:
                return 0
            if x not in range(m) or y not in range(n):
                return 1
            if (x, y, move) in memo:
                return memo[(x, y, move)] % mod
            memo[(x, y, move)] = solve(x, y - 1, move + 1) + solve(x - 1, y, move + 1) + \
                                 solve(x, y + 1, move + 1) + solve(x + 1, y, move + 1)
            return memo[(x, y, move)] % mod

        return solve(start_row, start_col, 0) % mod
