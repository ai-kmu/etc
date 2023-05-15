import math 

class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        dp = [100000] * (n+1)

        dp[1] = 1
        
        for i in range(n):
            square = i*i
            if square > n:
                break
            nums.append(square)
        
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                if i in nums:
                    dp[i] = 1
                else:           
                    dp[i] = min(dp[i-1]+1, dp[i-j*j]+ dp[j*j], dp[i])
                j += 1

        return dp[n]
