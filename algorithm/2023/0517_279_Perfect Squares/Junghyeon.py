'''
DP 동전교환 문제(냅색 알고리즘)와 동일
이때 동전들은 n보다 작은 perfect square number들로 구성
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        tmp = int(n**0.5)
        num = [i**2 for i in range(1, tmp+1)]

        for i in num:
            for j in range(i, n+1):
                if j-i >= 0:
                    dp[j] = min(dp[j], dp[j-i]+1)
                    
        return dp[-1]
