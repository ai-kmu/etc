from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance[0], entrance[1]
        r, c = len(maze), len(maze[0])
        moving = [(1,0),(0,1),(-1,0),(0,-1)]
        
        queue = deque()
        queue.append((x,y,0))
        
        maze[x][y] = "+"
        
        
        while queue:
            now_x, now_y, d = queue.popleft()
            
            # 자 이동해봅시다
            for _ in moving:
                dx = now_x + _[0]
                dy = now_y + _[1]
                if dx >= 0 and dx < r and dy >= 0 and dy < c:
                    # 도 착!
                    if (dx == 0 or dx == r-1 or dy == 0 or dy == c-1):
                        if maze[dx][dy] == ".":
                            return d+1

                    # 이 동 중 . . .
                    if maze[dx][dy] == ".":
                        maze[dx][dy] = "+"
                        queue.append((dx, dy, d+1))
        
        # 출구가 없는 경우 . . .
        return -1
