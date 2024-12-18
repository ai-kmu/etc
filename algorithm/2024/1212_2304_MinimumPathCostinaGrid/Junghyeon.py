# DP로 풀었습니다
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        original = [([0] * len(grid[0])) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                original[i][j] = grid[i][j]

        for r in range(1, len(grid)):
            for c in range(len(grid[0])):
                mini = float('inf')
                for j in range(len(grid[0])):
                    prev = original[r - 1][j]
                    mini = min(mini, grid[r - 1][j] + moveCost[prev][c])
                
                grid[r][c] += mini
        
        return min(grid[-1])
