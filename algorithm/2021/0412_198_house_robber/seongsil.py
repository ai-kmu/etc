# i=0, nums[i]  = 0
# i=1, nums[i] = max(nums[i-1], nums[i])
# i=2, nums[i] = max(nums[i-1], nums[i-2]+nums[i])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if i == 1: 
                nums[i] = max(nums[i], nums[0])
            else:
                nums[i] = max(nums[i-1], nums[i] + nums[i-2])
                
        return nums[len(nums)-1]
