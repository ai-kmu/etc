class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        minMax = [min, max]

        while len(nums) != 1:
            new_nums = [minMax[i % 2](*nums[2*i:2*(i+1)]) for i in range(len(nums) // 2)]
            nums = new_nums

        return nums[0]
