# 솔류션 참고 했습니다요
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums) - 2):
            diff = nums[i] - nums[i+1]
            for j in range(i+2, len(nums)):
                if nums[j-1] - nums[j] == diff:
                    c += 1
                else:
                    break
        return c
