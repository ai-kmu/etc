class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 행렬의 행, 열
        m, n = len(mat), len(mat[0])
        
        # 방향을 정의를 위해 정의
        direction = [0, 1, 0, -1, 0]

        # 값이 0인 셀의 좌표를 저장할 데크를 초기화합니다.
        q = deque([])
        
        # 행렬을 순회합니다.
        for r in range(m):
            for c in range(n):
                # 셀 값이 0이면 해당 좌표를 데크에 추가
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    # 셀 값이 1이면 -1로 설정하여 방문하지 않은 것으로 표시
                    mat[r][c] = -1
        
        # BFS
        while q:
            r, c = q.popleft()
            
            # 네 방향 탐색
            for i in range(4):
                nr, nc = r + direction[i], c + direction[i + 1]
                
                # 다음 셀이 행렬 범위 내에 있고 방문하지 않았으면 계속 진행
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1:
                    continue
                
                # 행렬에서 거리를 업데이트하고 새로운 셀을 데크에 추가
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))

        return mat
