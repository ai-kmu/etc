import math 

class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        dp = [0] * (n)

        for i in range(n):
            square = i*i
            if square > n:
                break
            nums.append(square)
        
        print(nums)
        for i in range(1, n):
            j = 1
            while j*j <= i:
                if i in nums:
                    dp[i] = 1
                else:                
                    dp[i] = min(dp[i-1]+1, dp[i-j*j] + 1)
                j += 1

        print(dp)
        return dp[n-1]
