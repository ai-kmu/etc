class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_new = []
        for i, j in enumerate(nums):
            nums_new.append([j, i])
        nums_new.sort()
        i = 0
        j = len(nums)-1
        result = []
        while i != j:
            # print(nums[i] + nums[j])
            if nums_new[i][0] + nums_new[j][0] == target:
                result.append(nums_new[i][1])
                result.append(nums_new[j][1])
                return result
            else:
                if nums_new[i][0] + nums_new[j][0] > target:
                    j -= 1
                else:
                    i += 1 
