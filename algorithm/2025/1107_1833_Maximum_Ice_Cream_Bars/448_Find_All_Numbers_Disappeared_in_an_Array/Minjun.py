class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        a = set(nums)
        for i in range(1, len(nums)+1):
            if i not in a:
                res.append(i)
        return res
