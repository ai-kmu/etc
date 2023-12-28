class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # dfs 활용한 방법
        # 0이 아닌 위치에서 이동하면서 0을 찾는 방법이 아니라
        # 0에서 시작해서 주변 값들의 거리를 초기화해나가는 방식
        # queue를 사용하기 때문에 거리가 0인 점에서 시작해서 거리가 점차 증가하게 된다.
        # 따라서 0이 아닌 위치에서 값이 초기화됐을 때 그 값보다 가까운 0이 있을 수는 없기 때문에
        # 거리를 비교하지 않아도 된다.
        m = len(mat)                    
        n = len(mat[0])
        answer = [[-1] * n for _ in range(m)]
        q = deque()
        
        # matrix의 0인 부분을 answer와 queue에 추가한다.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    q.append((i, j))
        
        while q:
            x, y = q.popleft()
            # 상하좌우 4개의 방향으로 이동한다.
            dif = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            
            for dx, dy in dif:
                new_x = x + dx
                new_y = y + dy
                # matrix에서 벗어날 경우 무시한다.
                if not (0 <= new_x < m) or not (0 <= new_y < n):
                    continue
                # 만약 이동한 위치가 아직 초기화되지 않았을 경우
                # 현재 위치에서의 값에 1을 더한 값으로 초기화한다.
                # 이동한 위치에서의 주변을 살펴보기 위해 이동한 위치를 queue에 추가한다.
                if answer[new_x][new_y] < 0:
                    answer[new_x][new_y] = answer[x][y] + 1
                    q.append((new_x, new_y))
        
        return answer
                    
        
