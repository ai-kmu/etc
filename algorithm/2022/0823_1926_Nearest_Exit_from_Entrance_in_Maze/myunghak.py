# 현재위치에서 시작한 후 현재 위치를 WALL로 바꾸고 BFS를 시작한다.

from collections import deque 

WALL = '+'
EMPTY = '.'
POS = '-'

class Solution:
    def nearestExit(self, maze, entrance):
        
        direction = ((0,1), (1,0), (-1,0), (0,-1))
        dp = deque([[entrance[0], entrance[1], 0]])  # dp에는 현재 위치와 시작점으로부터의 거리를 저장함
        
        def get_next_pos(pos):  # 현재위치로부터 갈수있는 곳을 deque에 넣기
            for dir in direction:
                if 0<= pos[0] + dir[0] < len(maze) and 0<= pos[1] + dir[1] < len(maze[0])  and maze[pos[0]+dir[0]][pos[1]+dir[1]] == EMPTY:
                    maze[pos[0] + dir[0]][pos[1] + dir[1]] = WALL
                    dp.append([pos[0] + dir[0], pos[1] + dir[1], pos[2]+1])
                    
                    if pos[0] + dir[0] == len(maze)-1 or pos[0] + dir[0] == 0 or \
                       pos[1] + dir[1] == len(maze[0])-1 or pos[1] + dir[1] == 0: 
                        return True
            return False
        
        maze[entrance[0]][entrance[1]] = WALL
        while(dp):
            current_pos = dp.popleft()
            if get_next_pos(current_pos):
                return current_pos[2] + 1
            
        
        
        return -1
