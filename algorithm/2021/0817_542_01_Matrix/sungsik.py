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


        # dynammic programming 방법
        # 한 위치에서 0이 아닐 경우 상하좌우의 값들 중 제일 작은 값으로 초기화하면서 진행하는 방법
        # 다만, 좌상단에서 우하단으로 순회한다고 가정했을 때
        # 한 위치에서 오른쪽과 아래쪽의 값은 아직 값을 세팅한 것이 아니기 때문에 
        # 오른쪽과 아래쪽의 값을 비교하는 것을 옳지 않다.
        # 우하단에서 좌상단으로 갈때도 마찬가지
        # 따라서 좌상단에서 우하단으로 갈때 왼쪽과 위쪽을 비교하고
        # 다시 우하단에서 좌상단으로 갈 때 오른쪽과 아래쪽을 비교하는 두번의 과정을 거쳐야 한다.
        # 주의할 점은 두번째 순회할 때에는 오른쪽과 아래쪽을 비교할때 첫번째 순회할때 고른 값과 비교하는 과정을 거쳐야
        # 상하좌우 4방향을 모두 참조할수 있다.
        m = len(mat)
        n = len(mat[0])
        _max = m + n
        
        # 좌상단에서 우하단으로 순회
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    up = mat[i-1][j] if i > 0 else _max
                    left = mat[i][j-1] if j > 0 else _max
                    # 위쪽과 왼쪽의 값 중 최솟값에 1만큼 더한다.
                    mat[i][j] = min(up, left) + 1
        
        # 우하단에서 좌상단으로 순회
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if mat[i][j] != 0:
                    down = mat[i+1][j] if i < m-1 else _max
                    right = mat[i][j+1] if j < n-1 else _max
                    # 아래쪽과 오른쪽의 값의 최솟값에 1을 더한 값과 현재 값 중 작은 값으로 세팅
                    mat[i][j] = min(mat[i][j], min(down, right) + 1)
        return mat
