from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_dict = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal_dict[i + j].append(nums[i][j])
        
        result = []
        for k in sorted(diagonal_dict.keys()):
            result.extend(reversed(diagonal_dict[k]))
        
        return result
