# 솔루션 참고: DP
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cost = [grid[0][:], [0] * n]
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if r > 0:
                    cost[r % 2][c] = cell + min(cost[1 - r % 2][j] + moveCost[i][c] for j, i in enumerate(grid[r - 1]))
        return min(cost[1 - m % 2])
