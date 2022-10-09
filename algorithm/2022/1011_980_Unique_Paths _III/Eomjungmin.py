# 테스트 케이스 오류 오답 나왔는데 아직 원인 못찾음

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid) # grid 행 개수
        n = len(grid[0]) # grid 열 개수
        ans = 0
        zero_count = 0
        count = 0
        
        for i in range(m):
            zero_count += grid[i].count(0)
            for j in range(n):
                if grid[i][j] == 1:
                    start_pos = (i,j)
        
        def dfs_backtracking(x, y, count, visited):
            nonlocal ans
            
            if (grid[y][x] == 2) and (count >= zero_count):
                ans += 1
                return
                
            for d in [(-1,0), (0,-1), (1,0), (0,1)]: # 상하좌우 이동
                dx = d[0]
                dy = d[1]
                
                # 이동 후 인덱스 벗어나지 않고 이동한 곳이 장애물이 아니며 방문 안했던 곳인 경우 dfs 이용
                # 그리고 방문 표시 후 backtracking을 위해 다시 방문 안했다고 표시
                if (0 <= x+dx < n) and (0 <= y+dy < m) and grid[y+dy][x+dx] != -1 and visited[y+dy][x+dx] == 0:
                    count += 1
                    visited[y+dy][x+dx] = 1
                    dfs_backtracking(x+dx, y+dy, count+1, visited)
                    visited[y+dy][x+dx] = 0 # backtracking
                    
        visited = [[0] * n for _ in range(m)] # 방문했던 곳 표시
        visited[start_pos[0]][start_pos[1]] = 1 # 시작점은 방문 표시
        dfs_backtracking(start_pos[0], start_pos[1], 0, visited) # dfs와 backtracking 이용
                
        return ans
