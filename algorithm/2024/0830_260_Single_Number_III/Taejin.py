from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        setA = set(nums[::2])
        setB = set(nums[1::2])
        
        ret = list(setA ^ setB)
        return ret
