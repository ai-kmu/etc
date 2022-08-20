from collections import deque


class Solution:
    '''
    BFS로 해결
    '''
    def nearestExit(self, maze, entrance):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        cnt = 0
        
        # deq에 x위치, y위치, cnt를 저장
        deq = deque([[entrance[0], entrance[1], cnt]])
        
        # 방문처리
        maze[entrance[0]][entrance[1]] = 'X'
        
        # BFS 탐색
        while deq:
            pos_x, pos_y, cnt = deq.popleft()
            # 위, 아래, 좌, 우로 탐색
            for i in range(4):
                nx = pos_x + dx[i]
                ny = pos_y + dy[i]
                if nx < 0 or nx > len(maze)-1 or ny < 0 or ny > len(maze[0])-1:
                    continue
                # .에 도착했을 때
                if maze[nx][ny] == '.':
                    # 방문처리를 하고
                    maze[nx][ny] = 'X'
                    # 탈출조건에 맞으면 탈출
                    if nx == 0 or nx == len(maze)-1 or ny == 0 or ny == len(maze[0])-1:    
                        return cnt+1
                    # 그렇지 않으면 다시 deq에 삽입
                    else:
                        deq.append([nx, ny, cnt+1])
        return -1
