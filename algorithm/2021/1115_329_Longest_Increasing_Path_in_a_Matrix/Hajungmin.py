class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 방향을 설정해준다
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # 만약 matrix가 없거나 matrix의 길이가 0이라면 0을 return 해준다.
        if (not matrix) or (len(matrix) == 0) : return 0
        m = len(matrix)
        n = len(matrix[0])
        # 메모이제이션을 위한 배열을 matrix와 동일한 크기로 0으로 초기화해준다.
        mem = [[0]*n for _ in range(m)]
        longest_dist = 0
        
        # dfs를 수행할 함수를 만든다. 이 때 입력으로는 matrix, matrix의 가로 세로 길이인 m, n, 현재 x,y,값인 i,j, 메모이제이션에 사용할 mem을 받는다
        def dfs(matrix, m, n, i, j, mem):
            #만약 메모이제이션 배열안에 미리 계산한 것이 있다면 그대로 return 해준다
            if mem[i][j] > 0: return mem[i][j]
            max_path = 0
            # 차례대로 방향을 돌아가며 길을 탐색한다.
            for dx, dy in dir:
                x = i + dx
                y = j + dy
                # x, y값의 범위를 matrix의 가로세로 길이보다 작은 경우, 0보다 큰 경우, 다음 값이 지금 값보다 큰 경우만 dfs를 통해 탐색한다.
                if (x >= 0 and y >= 0 and x < m and y < n and matrix[x][y] > matrix[i][j]):
                    # dfs로 탐색할 때는 max_path값과 dfs를 수행한 결과 중 max값을 사용한다.
                    max_path = max(max_path, dfs(matrix, m, n, x, y, mem))
            # 현재의 값을 mem에 메모한다
            mem[i][j] = max_path + 1
            # max_path에 1을 더해주고 return 한다.
            return max_path + 1
        
        for i in range(m):
            for j in range(n):
                # matrix를 모두 돌며 dfs를 수행해준다.
                path = dfs(matrix, m, n, i, j, mem)
                longest_dist = max(path, longest_dist)
                
        return longest_dist
