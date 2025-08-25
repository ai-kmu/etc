class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a, b = 0, 1
        
        while a <= b and b < len(nums):
            if nums[a] == nums[b]:
                b += 1
            else:
                nums[a+1] = nums[b]
                a += 1

        return a + 1   
