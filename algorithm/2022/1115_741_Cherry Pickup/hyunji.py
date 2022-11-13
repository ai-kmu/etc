# 오답...
# 좀 더 수정해볼게요..

from collections import deque

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        q = deque()
        answer = 0
        visited = [[0 for j in range(len(grid))] for i in range(len(grid))]
        dx = [1, 0]
        dy = [0, 1]

        q.append([0, 0])

        while q:
            x, y = q.popleft()

            for i in range(2):
                nx = x + dx[i]
                ny = y + dx[i]
                
                if nx < 0 or nx > len(grid) - 1 or ny < 0 or ny > len(grid) - 1:
                    continue

                if visited[nx][ny] == 1:
                    continue

                if grid[nx][ny] == 1:
                    answer += 1
                    q.append([nx, ny])
                    grid[nx][ny] = 0
                    visited[nx][ny] = 1
                    continue

                elif grid[nx][ny] == -1:
                    continue

                else:
                    q.append([nx, ny])
                    visited[nx][ny] = 1


        q2 = deque()
        visited2 = [[0 for j in range(len(grid))] for i in range(len(grid))]
        dx_2 = [-1, 0]
        dy_2 = [0, -1]

        q2.append([len(grid)-1, len(grid)-1])

        while q2:
            x, y = q2.popleft()

            for i in range(2):
                nx = x + dx_2[i]
                ny = y + dx_2[i]
                
                if nx < 0 or nx > len(grid) - 1 or ny < 0 or ny > len(grid) - 1:
                    continue

                if visited2[nx][ny] == 1:
                    continue

                if grid[nx][ny] == 1:
                    answer += 1
                    q2.append([nx, ny])
                    grid[nx][ny] = 0
                    visited2[nx][ny] = 1
                    continue

                elif grid[nx][ny] == -1:
                    continue

                else:
                    q2.append([nx, ny])
                    visited2[nx][ny] = 1

        return answer
