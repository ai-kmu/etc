"""
bottom-up dp 방식 풀이
idea : 요소값이 1일때 왼쪽, 위쪽, 대각선의 값을 보고 min인 값에 1 더해줌
예를들어 if (matrix[y][x] == 1) 일 때 dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]의 최솟값에 1을 더해 dp[y][x]를 업데이트
(최솟값이 0이라면 앞에 정사각형이 전혀 없는 것이기 때문에, 자기 자신 1이 정사각형의 최댓값이기 때문에 1 더해야 함)
이 방식으로 최대 변 길이를 구해서 면적을 구하겠다.
"""

class Solution:
    def maximalSquare(self, matrix):

        ROW= len(matrix) # matrix의 행의 길이
        COL= len(matrix[0]) #matrix의 열의 길이
        
        # dp 생성 (0으로만 구성된 (ROW)행 (COL)열 크기의 배열 생성)
        dp = [[0]*(COL) for x in range(ROW)]
        
        # 최대 변 길이
        max_edge = 0
        

        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == '1': 
                    # 요소 값이 1일 때 주변 값들과 비교해서 최소값으로 dp 업데이트
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
    
                    # 최대 변 update
                    max_edge = max(max_edge, dp[r][c])
                    
        # 면적을 계산하기 위해 변을 제곱
        return max_edge ** 2     
