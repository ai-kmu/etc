# 안풀려서 답보고 풀었습니다.
# 풀이는 안해주셔도 되요

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for len_subarray in range(2, n):
            for i in range(n - len_subarray):
                j = i + len_subarray
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

        # Return result
        return dp[0][n - 1]
