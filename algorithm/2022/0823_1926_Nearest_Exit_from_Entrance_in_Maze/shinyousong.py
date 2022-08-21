#시간초과, 어디서 줄여야 할지...
from collections import deque

class Solution:
    def BFS(self):
        while(True):
            if not self.q:
                return -1
            pos = self.q.popleft()
            ridx = pos[0]
            cidx = pos[1]
            step = pos[2]
            
            if (0 in pos[:2] or self.rlen-1 == ridx or self.clen-1 == cidx) and pos != self.entrance:
                return pos[2]
            
            self.visited[ridx][cidx] = '.'
            if self.rlen > ridx+1 and self.maze[ridx+1][cidx] != '+' and self.visited[ridx+1][cidx] == 0:
                self.q.append([ridx+1, cidx, step+1])
            if ridx > 0 and self.maze[ridx-1][cidx] != '+' and self.visited[ridx-1][cidx] == 0:
                self.q.append([ridx-1, cidx, step+1])
            if self.clen > cidx+1 and self.maze[ridx][cidx+1] != '+' and self.visited[ridx][cidx+1] == 0:
                self.q.append([ridx, cidx+1, step+1])
            if cidx > 0 and self.maze[ridx][cidx-1] != '+' and self.visited[ridx][cidx-1] == 0:
                self.q.append([ridx, cidx-1, step+1])
    
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 속성 정의
        self.maze = maze
        # 입구에 step 0 표시
        entrance.append(0)
        self.entrance = entrance
        # 입구 가로, 세로 길이 정의
        self.rlen = len(maze)
        self.clen = len(maze[0])
        # visited 생성
        self.visited = [[0 for c in range(self.clen)] for r in range(self.rlen)]
        # deque 생성
        self.q = deque()
        # deque 초깃값 부여
        self.q.append([i for i in self.entrance])
        # BFS
        step = self.BFS()
        return step
        
