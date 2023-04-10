class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # dfs와 backtracking을 활용한 풀이
        
        # 0은 visit한걸로 처리
        first_visited = [[not bool(i) for i in row] for row in grid]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        
        def dfs(location, visited, amount):
            max_amount = amount
            for dy, dx, in dirs:
                new_y, new_x = location[0] + dy, location[1] + dx
                
                if 0 <= new_y < m and 0 <= new_x < n and not visited[new_y][new_x]:
                    # backtracking
                    visited[new_y][new_x] = True
                    max_amount = max(max_amount, dfs((new_y, new_x), visited, amount + grid[new_y][new_x]))
                    visited[new_y][new_x] = False
            
            return max_amount
        
        max_amount = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    first_visited[row][col] = True
                    max_amount = max(max_amount, dfs((row, col), first_visited, grid[row][col]))
                    first_visited[row][col] = False
        return max_amount
