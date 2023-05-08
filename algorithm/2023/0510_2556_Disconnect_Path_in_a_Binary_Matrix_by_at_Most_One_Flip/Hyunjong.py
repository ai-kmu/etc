class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        start_end_point = [(0, 0), (m-1, n-1)]

        # dfs
        def dfs(i, j):
            # 다 돈 경우 즉 경로가 있음
            if(i == m-1 and j == n-1):
                return True

            # 길이 끝난 경우
            if(i >= m or j >= n or grid[i][j] == 0):
                return False

            # 길을 방문하고 있으면 방문 처리
            if (i, j) not in start_end_point:
                grid[i][j] = 0
            
            # 오른쪽 혹은 아래 방문
            return dfs(i + 1, j) or dfs(i, j + 1)

        # 두번 dfs 할거임, 그래서 처음 dfs때 말고 다른 경로가 있으면 False 아니면 True

        # 처음 방문때 경로가 없으면 True
        if(not dfs(0, 0)): 
            return True
        
        # 처음 두번째 방문때 경로가 없으면 True
        if(not dfs(0, 0)): 
            return True

        return False
