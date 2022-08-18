from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # m x n maze
        # empty '.', wall '+'
        # entrance [r, c]
        # if (r or c == 0) or (r == m or n == n)이면 탈출
        # bfs 사용해야함
        m, n = len(maze), len(maze[0])
        
        # bfs에 사용할 queue
        queue = deque([(entrance, 0)])
        
        # visit 체크
        visit = [[False for _ in range(n)] for _ in range(m)]
        visit[entrance[0]][entrance[1]] = True
        
        answer = 0
        while queue:
            pos, cnt = queue.popleft()
            # 4방향
            for dir_r, dir_c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_r, next_c = pos[0] + dir_r, pos[1] + dir_c # 다음 position
                
                # 범위 내 and 방문 X and maze == '.'
                if 0 <= next_r < m and 0 <= next_c < n and visit[next_r][next_c] is False and maze[next_r][next_c] == '.':
                    # 끝에 닿았을 때, 반환 => bfs이기 때문에 가장 빨리 하는 것이 정답
                    if next_r == 0 or next_c == 0 or next_r == m-1 or next_c == n-1:
                        return cnt + 1
                    else: # queue에 넣기
                        queue.append(((next_r, next_c), cnt+1))
                    visit[next_r][next_c] = True # 효율성을 위해 next로 visit 체크
                    
        return -1
            
            
        
