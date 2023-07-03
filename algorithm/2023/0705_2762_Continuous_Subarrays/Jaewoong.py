# 풀이실패...
class Solution:
    def continuousSubarrays(self, nums):
        n = len(nums)
        total = 0
        num_list = []
        
        for idx in range(n):
            while nums[idx] - nums[idx+1] <= 2:
                num_list.append(n)
            if idx == len(nums) - 2:
                break
