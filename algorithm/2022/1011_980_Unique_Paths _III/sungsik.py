class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        start_y, start_x, end_y, end_x = -1, -1, -1, -1
        total = m * n - 1
        
        # 순회를 하면서 시작점, 끝점, 장애물을 파악
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == 0:
                    continue
                elif item == -1:
                    visited[i][j] = True
                    # 장애물은 순회하지 않으므로 total에 1을 뺀다.
                    total -= 1
                elif item == 1:
                    start_y, start_x = i, j
                else:
                    end_y, end_x = i, j
        
        answer = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def explore(y, x, count):
            nonlocal answer
            for dy, dx in dirs:
                new_y, new_x = y + dy, x + dx
                if 0 <= new_y < m and 0 <= new_x < n and not visited[new_y][new_x] and grid[new_y][new_x] != -1:
                    # 새로 갈 위치가 끝점이고, 이미 모두 순회를 했을 경우
                    # answer에 1을 더한다.
                    if new_y == end_y and new_x == end_x and count == total:
                        answer += 1
                    # 일반적인 경우에는 visited를 True로 설정하고 방문한 다음 다시 False로 되돌리는
                    # backtracking을 수행
                    else:
                        visited[new_y][new_x] = True
                        explore(new_y, new_x, count+1)
                        visited[new_y][new_x] = False
        
        # 시작점을 방문한 다음 explore한다.
        visited[start_y][start_x] = True
        explore(start_y, start_x, 1)
        return answer
                    
