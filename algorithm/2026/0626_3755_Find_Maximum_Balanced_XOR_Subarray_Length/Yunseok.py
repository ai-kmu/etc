# 풀이 안해주셔도 됩니다

from typing import List

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        first = {(0, 0): -1}

        px = 0 
        bal = 0  
        ans = 0

        for i, x in enumerate(nums):
            px ^= x
            bal += 1 if x % 2 == 0 else -1

            state = (px, bal)

            if state in first:
                ans = max(ans, i - first[state])
            else:
                first[state] = i

        return ans
