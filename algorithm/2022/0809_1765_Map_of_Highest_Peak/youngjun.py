class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        # isWater 행렬의 행과 열 길이를 구해준다.
        cols, rows = len(isWater[0]), len(isWater)
        
        # 출력 행렬을 -1로 채워진 (rows,cols) 행렬로 만들어준다.
        out_mat = [[-1] * cols for _ in range(rows)]
        
        # 방문 행렬을 0으로 채워진 (rows,cols) 행렬로 만들어준다.
        visited = [[0] * cols for _ in range(rows)]
        
        # queue 생성
        bfs_q = deque()

        # 물이 있는 곳에 물을 채워준 후 visited에 표시, 위치를 queue에 넣어준다.
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    out_mat[i][j] = 0
                    visited[i][j] = 1
                    bfs_q.append((j, i))
        
        # bfs 정의
        def bfs(out_mat, visited, bfs_q):
            
            direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            while bfs_q:
                
                x, y = bfs_q.popleft()

                for dx, dy in direct:
                    
                    # 새로운 좌표 nx, ny 생성
                    nx = x + dx
                    ny = y + dy
                    
                    # nx, ny가 행렬 범위 안에 들어있고, 방문 표시가 되어 있지 않다면
                    if 0 <= nx < cols and 0 <= ny < rows and visited[ny][nx] == 0:
                        
                        # (x, y)의 값보다 1씩 크게 만들어준다.
                        out_mat[ny][nx] = out_mat[y][x] + 1
                        
                        # 방문 표시
                        visited[ny][nx] = 1
                        
                        # queue에 다시 넣는다.
                        bfs_q.append((nx, ny))

            return out_mat

        return bfs(out_mat, visited, bfs_q)
