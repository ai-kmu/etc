class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # DFS 함수
        def dfs(x, y, parent_x, parent_y, visited):
            # 만약 visited에 방문한 적이 있으면 cycle이 존재하는 것이기 떄문에
            # True 반환
            if visited[x][y]:
                return True

            # 현재 방문한 곳을 방문 처리
            visited[x][y] = True

            # 방향은 상하좌우로 설정
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 인덱스를 벗어나는지 확인
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue

                # 이전 노드와 같은 값이 아니면 무시
                if grid[nx][ny] != grid[x][y]:
                    continue

                # 이전 노드와 같은 값이면 재귀 호출
                if (nx, ny) != (parent_x, parent_y) and dfs(nx, ny, x, y, visited):
                    return True

            return False
        
        # 행, 열 요소들로 visited 리스트 생성
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # 각 요소들을 돌며 DFS 실행
        for i in range(rows):
            for j in range(cols):
                # 만약 현재 있는 위치가 방문처리되지 않았다면 DFS 실행
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, visited):
                        return True

        return False
        
