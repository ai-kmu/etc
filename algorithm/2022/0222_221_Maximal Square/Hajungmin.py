class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ### feedback: 문제 조건(1 <= m, n <= 300, m: 행의 길이, n: 열의 길이)이 입력 matrix의 행과 열이 반드시 1이상임으로 아래 조건식의 경우는 생략해도 무방
        if len(matrix) == 0:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        # Max가 최종 사각형의 한 변의 크기
        Max = 0
        
        dp = [[0 for i in range(col)] for j in range(row)]
        
        # 매트릭스 안이 0으로만 되어 있는지 확인하며 dp매트릭스를 원래 메트릭스와 같게 초기화해줌
        for i in range(row):
            if matrix[i][0] == '0':
                dp[i][0] = 0
            else : dp[i][0] = 1
            Max = max(Max, dp[i][0])
        
        for i in range(col):
            if matrix[0][i] == '0':
                dp[0][i] = 0
            else : dp[0][i] = 1
            Max = max(Max, dp[0][i]) 
        
        # 2중 for문을 돌며 dp를 수행
        # dp를 수행할 때는 (1,1)지점부터 왼쪽 위와 위쪽을 비교하고 이후에 왼쪽 수와 비교한 후에 1밖에 없다면 현재 좌표의 dp 매트릭스를 1더해주어 업데이트함
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = min(min(dp[i-1][j], dp[i-1][j-1] ), dp[i][j-1]) + 1
                    Max = max(Max, dp[i][j])
        
        return Max * Max
