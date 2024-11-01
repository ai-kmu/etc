class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        disappear = set(range(1, n+1))
        
        for num in nums:
            if num in disappear:
                disappear.remove(num)
        
        return list(disappear)
