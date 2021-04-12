class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums[0], nums[-1])
        
        nums[-3] += nums[-1]
        for i in range(4,len(nums)+1):
            nums[-i] += max(nums[-i+2], nums[-i+3])
        return max(nums[0],nums[1])
    
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return max(nums[0], nums[-1])
        
#         nums.reverse()
#         cumulative = nums[:2] + [nums[0] + nums[2]]
#         for i, n in enumerate(nums[3:]):
#             cumulative.append(n + max(cumulative[-2], cumulative[-3]))
#         return max(cumulative[-1], cumulative[-2])
    
    
