class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = list(range(1, len(nums)+1))
        ans = []
        nums = set(nums)
        for i in a:
            if i not in nums:
                ans.append(i)
        return ans
