class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, n in enumerate(nums):
            for j, k in enumerate(nums):
                if i != j:
                    if n + k == target:
                        return [i,j]
        
