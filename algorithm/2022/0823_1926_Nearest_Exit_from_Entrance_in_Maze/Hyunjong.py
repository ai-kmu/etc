# 오답 코드. test는 통과

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows = len(maze)
        cols = len(maze[0])
        direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visit = "v"
        
        maze[entrance[0]][entrance[1]] = visit
        queue = [(entrance, 0)]
        
        while queue:
            new_queue = []
            for (x, y), step in queue:
                if (x, y) != entrance and (x in (0, rows-1) or y in (0, cols-1)):
                    return step
                for dx, dy in direct:
                    nx, ny = x+dx, y+dy
                    if not (0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.'):
                        continue
                    maze[nx][ny] = visit
                    queue.append(((nx, ny), step+1))
            queue = new_queue
        return -1
