class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # unique path 찾기
        # 1-start , 2-end
        # 0-can walk, -1-can't walk
        # -1을 제외한 모든 칸을 밞아서 갈 수 있는 unique path
        # 재귀?
        
        m, n = len(grid), len(grid[0])
        path_sum = 0  # 들러야 하는 전체 칸 수
        start = None  # start point
        self.answer = 0  
        
        # update start and path_sum
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = [i, j]
                if grid[i][j] == 0:
                    path_sum += 1
        
        # dfs 재귀
        def dfs(curr_r, curr_c, cnt):
            # 해당 위치에 가지 못하는 경우, 끝
            if 0 > curr_r or curr_r >= m or 0 > curr_c or curr_c >= n or grid[curr_r][curr_c] < 0: 
                return
            # 조건에 맞출 경우
            if grid[curr_r][curr_c] == 2 and cnt == path_sum + 1:
                self.answer += 1
            
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                temp = grid[curr_r][curr_c]  # grid 값 저장
                next_r, next_c = curr_r + i, curr_c + j  # 위치 업데이트
                grid[curr_r][curr_c] = -1  # 방문 표시
                dfs(next_r, next_c, cnt + 1)  # 재귀 수행
                grid[curr_r][curr_c] = temp  # 다시 grid 값 복원
        
        # dfs 수행
        dfs(start[0], start[1], 0)
        return self.answer
