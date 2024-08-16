class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            n = nums.index(min(nums))
            nums[n] = -1*nums[n]

        return sum(nums)
