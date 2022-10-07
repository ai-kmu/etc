class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # 전체 깊이 확인
        temp = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp += grid[i][j]
        fin = len(grid[0]) * len(grid) + temp - 3
        
        # 현재 위치 찾기
        x = 0
        y = 0
        for i in range(len(grid)):
            if 1 in grid[i]:
                x = i
                break
        y = grid[x].index(1)
        
        # dfs
        def dfs(x, y, grid, depth):
            # 실패
            if depth == fin:
                return 0;
            cnt = 0
            # 방문처리
            grid[x][y] = -1
            # 성공 직전인지 확인
            if depth + 1 == fin:
                if (x > 0 and grid[x - 1][y] == 2) or (y > 0 and grid[x][y - 1] == 2) or\
                (x + 1 < len(grid) and grid[x + 1][y] == 2) or (y + 1 < len(grid[0]) and grid[x][y + 1] == 2):
                    return 1
            # 깃발은 미리 지나지 않도록 조건에서 제외
            if x > 0 and grid[x - 1][y] == 0:
                cnt += dfs(x - 1, y , grid, depth + 1)
                # 백트래킹
                grid[x - 1][y] = 0
            if y > 0 and grid[x][y - 1] == 0:
                cnt += dfs(x, y - 1 , grid, depth + 1)
                # 백트래킹
                grid[x][y - 1] = 0
            if x + 1 < len(grid) and grid[x + 1][y] == 0:
                cnt += dfs(x + 1, y, grid, depth + 1)
                # 백트래킹
                grid[x + 1][y] = 0
            if y + 1 < len(grid[0]) and grid[x][y + 1] == 0:
                cnt += dfs(x, y + 1, grid, depth + 1)
                # 백트래킹
                grid[x][y + 1] = 0
            return cnt
        # 실행
        return dfs(x, y, grid, 1)
