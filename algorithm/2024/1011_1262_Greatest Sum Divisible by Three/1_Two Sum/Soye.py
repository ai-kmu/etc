class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = 0
        b = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # print(i,j)
                if nums[i] + nums[j] == target:
                    a = i
                    b = j
        return [a,b]
