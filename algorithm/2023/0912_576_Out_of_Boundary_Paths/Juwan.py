class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        tmp = int(1e9 + 7)
        @cache
        def recur(row, col, moves):
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            if moves == 0:
                return 0

            return recur(row + 1, col, moves - 1) + recur(row - 1, col, moves - 1) + recur(row, col - 1, moves - 1) + recur(row, col + 1, moves - 1)
        
        return recur(startRow, startColumn, maxMove) % tmp
