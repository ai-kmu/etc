class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        num_set = set(nums)
        tmp = len(nums) - len(num_set)
        for i in range(1, len(nums)+1):
            if i not in num_set:
                ans.append(i)
                if len(ans) == tmp:
                    return ans
        return ans
        
