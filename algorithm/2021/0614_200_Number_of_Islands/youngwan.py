from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit_que = deque()                                  # 이어진 땅을 저장
        answer = 0                                           # 섬의 개수
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    visit_que.append((i,j))                  # 섬을 찾은 경우, visit_que에 저장
                    grid[i][j] = 0                           # 0으로 바꾸기
                    while visit_que:                         # 이어진 땅을 모두 찾기
                        x, y = visit_que.popleft()
                        if x-1 > -1:
                            if grid[x-1][y] == "1":
                                visit_que.append((x-1,y))
                                grid[x-1][y] = 0
                        if x + 1 < len(grid):
                            if grid[x+1][y] == "1":
                                visit_que.append((x+1, y))
                                grid[x+1][y] = 0
                        if y - 1 > -1:
                            if grid[x][y-1] == "1":
                                visit_que.append((x, y-1))
                                grid[x][y-1] = 0
                        if y + 1 < len(grid[0]):
                            if grid[x][y+1] == "1":
                                visit_que.append((x, y+1))
                                grid[x][y+1] = 0 
                    answer += 1                              # 새로운 땅을 찾은 경우에만 섬의 개수 
        return answer
