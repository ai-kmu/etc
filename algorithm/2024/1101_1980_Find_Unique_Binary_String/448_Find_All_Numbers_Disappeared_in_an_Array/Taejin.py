class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = [False] * len(nums)
        for i in nums:
            temp[i - 1] = True
            
        return [i + 1 for i in range(len(temp)) if not temp[i]]
