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
        
        ''' (feedback)
        결과값에서는 틀린 것은 없지만, 구조(의미)상 잘못된 부분 => row = 0 혹은 col = 0(첫번째 행과 열)일 경우 (index -1)의 의미는
        맨 오른쪽 열(col = 0)인 경우, 맨 아래쪽 행(row = 0)인 경우를 의미
        
        정사각형을 구성하는데 있어서, 첫번째 행과 열에서는 본인만 탐색하면 되지만, 본 코드에서는 떨어져있는 오른쪽 열과 맨 아래쪽 행을 같이 탐색해야 함으로 
        수정할 필요가 있음        
        (dp matrix를 0으로 초기화하여서 결과값에는 영향을 미치지는 않음, 
        만약 초기화 자체를 코드처럼 0으로 matrix로 초기화하는 것이 아니라, input matrix 값을 가져오는 식으로 초기화했다면 error 발생)
        
        해결방안 1. 이중 for문 내에서 if 문 코드 홀용해 첫번째 행과 열일 경우에는 본인만 탐색하는 코드 생성 => 예: 임종수님
        해결방안 2. 이중 for문 전에 첫번째 행과 열을 먼저 (자기자신을) 탐색해서 matrix에 저장하는 방법 -> 예: 하정민님
        ''' 
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == '1': 
                    # 요소 값이 1일 때 주변 값들과 비교해서 최소값으로 dp 업데이트
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
    
                    # 최대 변 update
                    max_edge = max(max_edge, dp[r][c])
                    
        # 면적을 계산하기 위해 변을 제곱
        return max_edge ** 2     
