from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        
        queue = deque() # bfs 구현을 위한 deque 변수 선언
        queue.append(entrance+[0]) # 시작점 추가(뒤에 0은 이동거리를 나타냄. 시작점은 당연히 0)
        
        visited = [[False for i in range(n)] for j in range(m)] # 방문했다는 표시를 기록하는 array
        visited[entrance[0]][entrance[1]] = True # 시작점은 True
        
        
        # 시작점에서 이동할 수 있는 곳으로 상하좌우 이동
        # 이동하다가 출구를 만나는 순간 바로 그때의 거리값 d를 return 하도록 함
        # 만약 반복문을 돌아도, queue 다 없어진 후에도 답이 없으면 -1 리턴
        while queue:
            r, c, d = queue.popleft()
            if (r == 0 or r == m-1 or c == 0 or c == n-1) and d != 0:
                return d
            else:
                if (r-1 >= 0):
                    if visited[r-1][c]==False and maze[r-1][c] == ".":
                        visited[r-1][c] = True
                        queue.append([r-1, c, d+1])
                if (r+1 < m):
                    if visited[r+1][c]==False and maze[r+1][c] == ".":
                        visited[r+1][c] = True
                        queue.append([r+1, c, d+1])
                if (c-1 >= 0):
                    if visited[r][c-1]==False and maze[r][c-1] == ".":
                        visited[r][c-1] = True
                        queue.append([r, c-1, d+1])
                if (c+1 < n):
                    if visited[r][c+1]==False and maze[r][c+1] == ".":
                        visited[r][c+1] = True
                        queue.append([r, c+1, d+1])
        return -1
