from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
    
        Q = deque()
        Q.append([entrance[0], entrance[1], -1])

        while Q:
            
            cur_i, cur_j, distance = Q.popleft()

            # 탈출조건
            if cur_i < 0 or cur_j < 0 or cur_i >= len(maze) or cur_j >= len(maze[0]):
                # 처음 위치이면 탈출안함
                if distance == 0:
                    continue
                return distance

            # 벽으로 이동하지 않음
            if maze[cur_i][cur_j] == '+':
                continue

            # 방문처리('.'으로만 이동함) 
            if maze[cur_i][cur_j] != '.':
                continue
            maze[cur_i][cur_j] = distance
            
            # 이동
            for dy, dx in [[1, 0],[0, 1],[-1, 0],[0, -1]]:
                Q.append([cur_i + dy, cur_j + dx, distance + 1])
        
        return -1
