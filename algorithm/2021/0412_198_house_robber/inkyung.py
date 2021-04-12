class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] = max(nums[i-2] + nums[i], nums[i-3] + nums[i])
        return max(nums)
            
