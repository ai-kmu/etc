class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        num_set = set()
        for i in range(1, l+1):
            num_set.add(i)
        for v in nums:
            if v in num_set:
                num_set.remove(v)
        
        return list(num_set)
        
