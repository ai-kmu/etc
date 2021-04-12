class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)): # 모든 nums를 돌면서
            if i > 1: # 0부터 i-2까지 중에 max인 것을 num[i]에 더함(update) ==> sub problem
                nums[i] += max(nums[0:i-1])
        
        return max(nums)
