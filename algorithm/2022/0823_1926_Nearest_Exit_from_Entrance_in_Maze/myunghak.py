from collections import deque 

WALL = '+'
EMPTY = '.'
POS = '-'

class Solution:

    def nearestExit(self, maze, entrance):
        
        direction = ((0,1), (1,0), (-1,0), (0,-1))
        dp = deque([[entrance[0], entrance[1], 0]])
        
        def get_next_pos(pos):
            
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
