# i번째에서 최대값을 가지려면 nums[i] + max(dp[i-k : i))를 구하면 된다.
# 여기서 i는 i-1번째 까지의 최대값들이 저장되어 있는 배열이다.

import numpy as np

class Solution:
    def maxResult(self, nums, k):
        dp = np.array(nums)
        for i in range(1, len(nums)):
            dp[i] = dp[i] + np.max(dp[max(0, i-k):i])

        return dp[-1]
