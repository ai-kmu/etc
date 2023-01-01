class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = []
        dp[0][0] = nums[0]

        ans = sum(nums)

        return ans
