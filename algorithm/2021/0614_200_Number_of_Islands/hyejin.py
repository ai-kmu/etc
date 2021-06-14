from collections import deque

# visit를 사용하지 않고, grid에 직접 방문표시 (-1)
# bfs는 time limit 초과, dfs는 통과 deque에서 popleft가 느림.

class Solution:    
    def dfs(self, grid, pos):
        m, n = len(grid), len(grid[0])
        queue = deque([pos])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.pop()
            grid[r][c] = -1 # 방문한 곳은 -1로 체크(visit 대신)
            for dx, dy in direction: # 가능한 지역
                next_r, next_c = r+dx, c+dy
                if (0 <= next_r < m) and (0 <= next_c < n):
                    if grid[next_r][next_c] == "1":
                        queue.append((r+dx, c+dy))
                    
        return grid
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs로 island 찾기
        m, n = len(grid), len(grid[0])
        answer = 0
        # 모든 원소를 탐색
        for r in range(m):
            for c in range(n):
                # 방문하지 않았던 position이고, 1이라면 dfs 탐색
                if grid[r][c] == "1":
                    grid = self.dfs(grid, (r, c))
                    answer += 1
        
        return answer
