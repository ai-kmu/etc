class Solution:
    def __init__(self):
        self.rets = []
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        if nums not in self.rets:
            self.rets.append(nums)

            for i in range(len(nums)):
                self.subsetsWithDup(nums[:i] + nums[i+1:])

        return self.rets
