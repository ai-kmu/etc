# 솔루션 참고....

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        tmp = {(0, 0): -1}
        diff = 0
        pxor = 0
        ans = 0

        for i, x in enumerate(nums):
            pxor ^= x

            if x % 2 == 0:
                diff += 1
            else:
                diff -= 1
            
            state = (pxor, diff)
            
            if state in tmp:
                ans = max(ans, i - tmp[state])
            else:
                tmp[state] = i


        return ans
