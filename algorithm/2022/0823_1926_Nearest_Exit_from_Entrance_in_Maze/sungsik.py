from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # bfs 문제
        queue = deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(maze), len(maze[0])
        
        y, x = entrance
        maze[y][x] = "+"
        queue.append((y, x, 0))
        
        while queue:
            y, x, dist = queue.popleft()
            
            for dy, dx in dirs:
                new_y, new_x = y + dy, x + dx
                # index가 범위에서 벗어날 경우 모서리로 간주
                try:
                    if new_y < 0 or new_x < 0:
                        raise IndexError
                    if maze[new_y][new_x] == ".":
                        maze[new_y][new_x] = "+"
                        queue.append((new_y, new_x, dist+1))
                except IndexError:
                    # 시작점이 모서리인 경우 처리
                    if dist:
                        return dist
                    continue
        
        return -1
