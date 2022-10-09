# DFS로 완전 탐색한다.
# DFS로 탐색 중 모든 공간을 탐색한 경우만 answer에 포함시킨다.

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        empty_space = r * c - 1
        self.ans = 0
        
        # grid를 전부 탐색하여 시작위치, target의 위치, 빈공간의 개수를 알아낸다.
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == -1:
                    empty_space -= 1
                elif grid[i][j] == 2:
                    target = (i, j) 
                    
        # DFS 알고리즘
        def dfs(walk, y,x):
            if 0<=y<r and 0<= x < c and grid[y][x] != -1:
                # 현재 위치가 목적지임과 동시에 모든 공간을 탐색했으면 ans에 1을 더해주고 목적지이기만 하면 함수를 종료해준다.
                if (y, x) == target:
                    if walk == empty_space:
                        self.ans +=1
                    return
                elif abs(y-target[0]) + abs(x - target[1]) > empty_space - walk: # target까지의 남은 거리가 현재 움직일수 있는 횟수를 초과하면 함수를 종료한다
                    return

                # 4방향으로 탐색을 시작한다. 단 탐색 전 현재 위치로 다시 돌아오지 않도록 grid를 -1로 초기화 해준다.
                grid[y][x] = -1
                dfs(walk+1, y-1, x)
                dfs(walk+1, y+1, x)
                dfs(walk+1, y, x-1)
                dfs(walk+1, y, x+1)
                grid[y][x] = 0
                
        dfs(0, start[0], start[1])
        
        return self.ans
