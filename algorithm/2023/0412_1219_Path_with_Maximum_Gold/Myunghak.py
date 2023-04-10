# 답보고 풀었습니다.
# 리뷰 안해주셔도 되요

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, gold, visited):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or visited[i][j] or grid[i][j] == 0:
                return gold

            visited[i][j] = True
            max_gold = gold
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                max_gold = max(max_gold, dfs(x, y, gold + grid[i][j], visited))
            visited[i][j] = False

            return max_gold

        max_gold = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_gold = max(max_gold, dfs(i, j, 0, visited))

        return max_gold
