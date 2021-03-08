class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        # n=2이면 최대가 1밖에 안되기 때문에 idx=2까지는 1로 채워줌
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            temp = []
            for j in range(1,i // 2 + 1):
                # i보다 작은 j값과 dp에 이미 저장한 값 중 큰값과
                # i-j 값과 dp[i-j] 값을 곱한 것을 쌓아 주고 그 중 큰값을 dp에 저장
                temp.append(max(j, dp[j]) * max(i - j, dp[i-j])) 
            dp[i] = max(temp)
        return dp[n]
