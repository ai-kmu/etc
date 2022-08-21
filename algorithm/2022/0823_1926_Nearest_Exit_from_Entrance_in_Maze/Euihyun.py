from collections import deque

# BFS로 구현해보려고 했는데 구현 못했습니다.. 

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        n = len(maze)
        m = len(maze[0])
        
        visit = deque() # x좌표, y 좌표, depth
        a, b = entrance
        
        maze[a][b] = '+'
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            visit.append([nx, ny, 1])
        
        while visit:
            x, y, depth = visit.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny <0 or ny >= m:
                    continue
                
                if maze[nx][ny] == '+':
                    continue
                
                if nx == 0 or nx == n - 1 or ny == 0 or ny == m - 1:
                    return depth
                
                
                if maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    visit.append([nx, ny, depth + 1])
                
        return -1

