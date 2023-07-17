class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        N = len(grid)
        M = len(grid[0])

        visited = [[False for i in range(M)] for j in range(N)]  # 여기까지 일반 DFS 세팅
        
        flag = False # Cycle 탐색 시 flag
        
        def isVal(x, y): # 그냥, 탐색할 위치가 Grid 내에 있는 지 확인하려는 것

            if 0 <= x < N and 0 <= y < M:
                return True
            return False

        
        def dfs(x, y, x_p, y_p):
            
            nonlocal flag  # nonlocal을 설정해줘야 작동함
          
            visited[x][y] = True # 방문하면 방문 처리

            for a, b, in zip(dx, dy):

                newX, newY = x + a, y + b # 새로 탐색할 위치

                if isVal(newX, newY) and grid[x][y] == grid[newX][newY] and not (x_p == newX and y_p == newY):
                  # isVal : Grid 내에 새 좌표가 있는가
                  # grid[x][y] == grid[newX][newY] : 동일한 문자에 대한 탐색을 하고 있는가
                  # not (x_p == newX and y_p == newY) : 새로운 좌표가 직전의 좌표와 달라야함.
                  # visited를 통해서 cycle의 여부를 확인할 것이기 때문에 visited로 dfs의 depth를 더 내려가는 조건을 보는 게 아님
                  # 따라서 not (x_p == newX and y_p == newY)를 통해 직전 좌표가 아니라 다시 visited로 돌아왔을 때 Cycle이 있다는 판단

                    if visited[newX][newY]: # 만약 직전 좌표 말고도 visited로 돌아왔다면 cycle이 존재하는 것으로 판단
                        flag = True
                        return

                    else: # 아직 방문 안한 노드가 있다면 dfs
                        dfs(newX, newY, x, y)

            return

        for i in range(N):
            for j in range(M): 
                if not visited[i][j]:
                    dfs(i, j, -1, -1)

        return flag
