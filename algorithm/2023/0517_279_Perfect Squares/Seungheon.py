class Solution:
    def numSquares(self, n: int) -> int:
        
        # 제곱값 리스트
        square_list = [i**2 for i in range(101)]

        # idx : 만들어진 숫자, valuew : 사용된 개수
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        # dp 테이블 채우기
        for i in range(1, n+1):
          
            min_count = float('inf')
            # 제곱값들 순회하며 사용 될 수 있으면 사용
            for j in square_list:
                if i-j >= 0:
                    dp[i] = min(dp[i], dp[i-j] + 1) 

        return dp[-1]
                
