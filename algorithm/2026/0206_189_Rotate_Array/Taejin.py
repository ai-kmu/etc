class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (k % len(nums)) == 0:
            return
        
        dummy = nums[-(k % len(nums)):]
        nums[(k % len(nums)):] = nums[:-(k % len(nums))]
        nums[:(k % len(nums))] = dummy
        
