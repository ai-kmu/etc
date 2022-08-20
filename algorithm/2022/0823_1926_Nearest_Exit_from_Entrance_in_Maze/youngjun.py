class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = [[0]*len(maze[i]) for i in range(len(maze))]
        q = deque()

        q.append((entrance, 0))
        visited[entrance[0]][entrance[1]] = 1

        direct = [[-1,0],[1,0],[0,1],[0,-1]]

        while q:
            position, cnt = q.popleft()
            r, c = position[0], position[1]
            for dr, dc in direct:
                nr = r + dr
                nc = c + dc
                if 0 <= nr <= len(maze) - 1 and 0 <= nc <= len(maze[0]) - 1 and visited[nr][nc] == 0 and maze[nr][nc] == ".":
                    if nr == 0 or nc ==0 or nr == len(maze) - 1 or nc == len(maze[0]) - 1:
                        visited[nr][nc] = 1
                        cnt += 1
                        return cnt
                    else:
                        visited[nr][nc] = 1
                        q.append(([nr,nc],cnt + 1))
        
        return -1
