class Solution:
    def dfs(self, grid, row, col, visited, prev_row, prev_col, prev):

        # 범위를 넘을 때
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != prev:
            return False

        # 방문한 곳을 다시 방문했을 때
        if visited[row][col]:
            return True
        
        # 방문 처리
        visited[row][col] = True
        
        # 방향
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 방향 이동
        for dx, dy in directions:
            # 새로운 위치
            new_row, new_col = row + dx, col + dy
            # 이전 위치에서 현재 위치로 이동한 경우를 제외(다시 체크하는 경우 제외)
            if new_row == prev_row and new_col == prev_col:
                continue

            # 방문한 곳을 다시 방문했을 때
            if self.dfs(grid, new_row, new_col, visited, row, col, grid[row][col]):
                return True
        
        return False
    
    def containsCycle(self, grid):

        m, n = len(grid), len(grid[0])
        # 방문 처리 그리드 설정
        visited = [[False] * n for _ in range(m)]
        
        # 반복
        for i in range(m):
            for j in range(n):
                # 방문하지 않았을 때
                if not visited[i][j]:
                    # dfs 순환
                    if self.dfs(grid, i, j, visited, -1, -1, grid[i][j]):
                        return True
        return False
