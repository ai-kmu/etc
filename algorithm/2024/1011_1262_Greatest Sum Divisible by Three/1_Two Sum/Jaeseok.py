class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = dict()
        for i, v in enumerate(nums):
            comp = target - v
            if comp in comp_dict:
                return [comp_dict[comp], i]
            comp_dict[v] = i
