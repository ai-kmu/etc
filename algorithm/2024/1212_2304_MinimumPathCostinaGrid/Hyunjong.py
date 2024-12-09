class Solution(object):
    def minPathCost(self, grid, moveCost):
        # grid[i][j] : i 번째 행과 j 번째 열의 cell 값
        # moveCost[i][j] : 값이 i인 cell에서 다음 행의 j번째 열로 이동할 때 소요되는 비용
        
        # 초기화
        # dp : 현재 행에서 다음 cell까지의 최소 비용을 저장할 DP 배열 
        # 마지막 열에서 최소값을 찾으므로 하나의 열에서 계속 업데이트 하면 됨
        m, n = len(grid), len(grid[0])
        dp = grid[0]

        # 두 번째 행부터 마지막 행까지 반복
        for i in range(1, m):

            # 다음 행에서의 최소 비용 초기화
            new_dp = [float('inf')] * n

            # 현재 행 과 다음 행의 완전 연결한 후 계산 (n X n)
            # 현재 행의 각 cell 반복
            for j in range(n):
                # 다음 행의 각 cell 반복
                for k in range(n):
                    # 비용 계산 : 현재 cell 값 + moveCost 값 + 다음 cell의 값 
                    #   i는 다음 행의 index, j는 현재 행에서 열의 index, k는 다음 행에서 열의 index
                    #   이때 moveCost는 현재 cell의 위치의 값에서 다음 행에서 열에 대한 값임
                    #   따라서 인덱스 [현재 cell 값, 다음 열 위치]는 [gird[i-1][j], [k]]임
                    new_dp[k] = min(new_dp[k], dp[j] + moveCost[grid[i - 1][j]][k] + grid[i][k])
            # 두 행간의 연산이 다 끝나면 업데이트
            dp = new_dp
        # 마지막 행에서 최소 비용 반환
        return min(dp)
