class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add padding of 1 to beginning and end of nums array
        nums = [1] + nums + [1]
        n = len(nums)

        # Initialize dp array with 0's
        dp = [[0] * n for _ in range(n)]

        # Perform dynamic programming
        for len_subarray in range(2, n):
            for i in range(n - len_subarray):
                j = i + len_subarray
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

        # Return result
        return dp[0][n - 1]
