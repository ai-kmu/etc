from collections import defaultdict

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)

        result =[]

        max_nums = max(nums)
        max_nums = max(max_nums, len(nums))

        for i in nums:
            d[i] = 1

        for i in range(1, max_nums+1):
            if i not in d.keys():
                result.append(i)
        
        return result
