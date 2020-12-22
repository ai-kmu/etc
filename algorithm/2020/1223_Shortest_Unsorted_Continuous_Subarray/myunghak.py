class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s, l = 0, 0
        start = False
        for i,n in enumerate(sorted(nums)):
            if n != nums[i] and not start:
                start = True
                s,l= i,i
            elif n != nums[i]:
                l=i+1
        return l-s
