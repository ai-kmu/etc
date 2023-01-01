from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        idx = deque([0])

        for i in range(1, n):
            while idx[0] < i - k:
                idx.popleft()
            nums[i] = nums[idx[0]] + nums[i]
            while idx and nums[idx[-1]] < nums[i]:
                idx.pop()
            idx.append(i)
        
        return nums[-1]
