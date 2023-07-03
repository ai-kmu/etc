from collections import deque

class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            s, e = i, i
            minNum, maxNum = nums[s], nums[s]

            while e < len(nums):
                if nums[e] > maxNum:
                    maxNum = nums[e]
                
                if nums[e] < minNum:
                    minNum = nums[e]
            
                if maxNum - minNum <= 2:
                    ans += 1
                else:
                    break

                e += 1
                
        return ans
