class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 동적 계획법 중 bottom-up 방식으로 풀이
        # matrix 요소값이 1일 때 그 요소의 왼쪽과 위쪽, 그리고 왼쪽 위 대각선 방향의 값을 보고
        # 그 최소값의 1을 dp배열에 저장.
        # 그리하여 현재 포인트에서 가장 크게 만들 수 잇는 사각형의 변 길이를 저장
        n = len(matrix) # 세로 변 길이
        m = len(matrix[0]) # 가로 변 길이
        dp = [[0] * (m+1) for _ in range(n+1)] # 2차원 dp배열 선언
        ans = 0 # 최대 변 길이
        
        # dp 배열 순회하여 최대 사각형 변 길이를 dp배열에 저장
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
            ans = max(ans, max(dp[i+1]))
            
        return ans*ans
