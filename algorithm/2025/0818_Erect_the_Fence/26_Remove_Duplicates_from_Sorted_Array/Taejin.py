from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        i = 0
        k = len(set(nums))
        for _, v in cnt.items():
            for j in range(1, v):
                nums[i + j] = float('inf')
            i += v

        nums.sort()
        return k
            

