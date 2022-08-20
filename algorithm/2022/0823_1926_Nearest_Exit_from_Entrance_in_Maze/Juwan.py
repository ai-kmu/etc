from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m = len(maze)
        n = len(maze[0])
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        visit = deque([]) # BFS 구현
                
        maze[entrance[0]][entrance[1]] = '+' # 시작점은 방문했다는 처리
        
        for i, j in zip(dx, dy):
            
            x = entrance[0] - i
            y = entrance[1] - j
            
            if 0 <= x < m and 0 <= y < n:
                visit.append([x, y, 1]) # 시작점으로부터 먼저 한번 BFS 수행
        
        while visit:
            
            i, j, d = visit.popleft()
            
            if maze[i][j] == '+':
                continue
            
            maze[i][j] = '+' # 방문 처리
            
            if i == 0 or j == 0 or i == m -1 or j == n - 1:
                
                return d # BFS의 장점. depth를 늘려가면서 너비 우선 탐색을 하므로, 조건에 맞는 가장 첫번째 케이스가 정답이므로 바로 return
            
            for a, b in zip(dx, dy):
                
                x = i - a
                y = j - b
            
                if 0 <= x < m and 0 <= y < n:
                    visit.append([x, y, d + 1])
                  
        # 만약 BFS를 수행해도 결과를 찾을 수 없으면 출구가 없는거.
        return -1
        
