class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            a = min(nums)
            idx = nums.index(a)
            nums[idx] = -a
        
        return sum(nums)
