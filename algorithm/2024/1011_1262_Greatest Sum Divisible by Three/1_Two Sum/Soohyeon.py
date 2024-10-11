class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]