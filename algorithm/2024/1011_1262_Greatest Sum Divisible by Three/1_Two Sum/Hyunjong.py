class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        tmp = nums[i] + nums[j]
                        if tmp == target:
                            return [i, j]
