class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[p] = nums[i]
                p += 1
        return p
