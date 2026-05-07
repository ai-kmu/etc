# 솔루션 참고...

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = nums[i]
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])

        return dp[-1] >= 0

