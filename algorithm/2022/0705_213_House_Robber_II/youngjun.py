class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        #dp1은 nums[1]부터 nums[n-1]까지, dp2는 nums[2]부터 nums[n]까지 터는 것을 나타냄
        dp1 = 0
        dp2 = 0
