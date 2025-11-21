class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            nums[idx] = -abs(nums[idx])

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        
        return ans
