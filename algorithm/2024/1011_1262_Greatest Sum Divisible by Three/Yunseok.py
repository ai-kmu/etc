class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -9999, -9999]
        
        for number in nums:
            current = dp[:]
            for rem in range(3):
                new_rem = (current[rem] + number) % 3
                new_sum = current[rem] + number
                dp[new_rem] = max(dp[new_rem], new_sum)
        
        return dp[0]
