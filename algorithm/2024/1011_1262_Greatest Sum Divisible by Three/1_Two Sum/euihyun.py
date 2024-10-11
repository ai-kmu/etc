class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        
        return ans
            
