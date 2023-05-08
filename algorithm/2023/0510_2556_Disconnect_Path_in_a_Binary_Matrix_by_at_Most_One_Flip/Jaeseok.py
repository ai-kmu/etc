class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        # (0,0)과 (n-1, m-1)은 무조건 1이기 때문에 경로 탐색 문제로 생각할 수 있음
        # 중복되지 않은 경로(2번째 경로)로 오른쪽 아래에 도달할 수 있다면 False, 아니라면 True
        n, m = len(grid), len(grid[0])
        # flag는 끝까지 도달할 수 있는지 확인하는 bool
        self.flag = False

        def dfs(x, y):
            # 이미 끝까지 도달했다면 나머지 경로는 탐색하지 않음
            # 남은 경로를 새로 확인하기 위함
            if self.flag:
                return
            if x == n-1 and y == m-1:
                self.flag = True
                return
            # matrix 밖으로 벗어나는 것을 방지
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            # 만약에 아직 탐색하지 않은 곳이라면 0으로 만들고 추가 탐색
            if grid[x][y] != 0:
                grid[x][y] = 0
                dfs(x+1, y)
                dfs(x, y+1)

        # (0,0)부터 탐색 시작
        dfs(0, 0)
        # 탐색이 끝났으면 추가 탐색을 위해 (0,0)부터 다시 탐색할 수 있게 만듬
        grid[0][0] = 1
        self.flag = False
        # 2번째 탐색에서도 마지막까지 도달했으면 False
        dfs(0, 0)
        return False if self.flag else True
