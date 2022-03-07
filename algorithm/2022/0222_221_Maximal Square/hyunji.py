# Dynamic Programming을 이용한 문제

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        # base case: 행과 열의 길이가 0인 배열의 경우 
        rows = len(matrix)
        cols = len(matrix[0])
        
        ### feedback: 문제 조건상 입력 matrix 행과 열이 반드시 1이상이기 때문에 생략해도 무방
        if rows == 0 or cols == 0:
            return 0
        
        # dp 행렬을 생성해주기
        Dp = [[0]*(cols+1) for x in range(rows+1)]
        

        max_len = 0
        for i in range(rows):
            for j in range(cols):
                
                # 배열을 탐색하다가 1을 발견한 경우
                # 왼쪽, 왼쪽 대각선, 위 방향에서 최소값을 찾아서 1을 더해준다
                # 이런 방식으로 가장 긴 1로 구성된 사각형의 변의 길이를 저장해주면 된다.
                if matrix[i][j] == "1":
                    Dp[i+1][j+1] = min(Dp[i][j], Dp[i][j+1], Dp[i+1][j]) + 1
                    max_len = max(max_len, Dp[i+1][j+1])

        return max_len**2
