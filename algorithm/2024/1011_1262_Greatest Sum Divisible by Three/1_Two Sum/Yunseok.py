class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx_i, elem_i in enumerate(nums):
            for idx_j, elem_j in enumerate(nums):
                if idx_i == idx_j:
                    continue

                if elem_i + elem_j == target:
                    return [idx_i, idx_j]
