class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # 모든 노드가 연결된 격자형태의 그래프임
        # 따라서 방문 여부를 기록하고 탐색시 이전 노드를 방문하지 않는다면
        # 재방문한 노드가 생길경우 사이클

        self.n = len(grid) # Height
        self.m = len(grid[0]) # Width
        self.grid = grid 
        self.visited = set()
        
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) not in self.visited: # 방문하지 않았으면 dfs 시작
                    if self.dfs(i, j, (-1, -1)) == True: # 사이클 발견
                        return True # 사이클이 하나라도 나오면 True


        return False # 사이클이 하나도 없으면 False

    def dfs(self, y, x, p):
        if (y, x) in self.visited: # 재방문 == 사이클
            return True
        
        self.visited.add((y, x)) 
        previous = (y, x) # 다음 dfs 시행시 이전 노드의 좌표
        current = self.grid[y][x]

        for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ny, nx = y + dy, x + dx

            if 0 <= ny < self.n and 0 <= nx < self.m and (ny, nx) != p and current == self.grid[ny][nx]:
                if self.dfs(ny, nx, previous) == True:
                    return True

        return False
