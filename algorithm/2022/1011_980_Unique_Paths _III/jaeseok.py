class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        answer = 0
        rows = len(grid)
        cols = len(grid[0])
        # 모든 갈 수 있는 길을 다 가야 하므로 경로의 수는 행의 수 x 열의 수 - 1
        path_num = rows * cols - 1
        for i in range(rows):
            for j in range(cols):
                # 시작 지점 확인하고 저장
                if grid[i][j] == 1:
                    start_x = i
                    start_y = j
                # 가야 하는 경로의 수에서 장애물이 있는 지역의 수를 빼줌
                elif grid[i][j] == -1:
                    path_num -= 1

        def dfs(x, y, n):
            nonlocal answer
            # 갈 수 없는 곳이나 장애물이 있는 지역이면 종료
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == -1:
                return
            # 도착했을 때
            if grid[x][y] == 2:
                # 남은 경로의 수가 0이면 unique path
                if n == 0:
                    answer += 1
                # 그렇지 않은 경우면 종료
                return
            # 도달한 곳은 다시 갈 수 없도록 만듬
            grid[x][y] = -1
            # 다음 경로 탐색 진행
            dfs(x - 1, y, n - 1)
            dfs(x, y - 1, n - 1)
            dfs(x + 1, y, n - 1)
            dfs(x, y + 1, n - 1)
            # 진행하는 경로 탐색이 끝나면 다시 갈 수 있게 만들어줌
            grid[x][y] = 0

        dfs(start_x, start_y, path_num)

        return answer
