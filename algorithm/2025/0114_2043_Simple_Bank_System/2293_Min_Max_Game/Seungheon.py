class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def minmax(nums):
            if len(nums) == 1:
                return nums[0]
            else:
                new_nums = []
                half = len(nums)/2/2
                for j in range(len(nums)/2):
                    i = 2*j
                    if i % 2 == 0:
                        new_nums.append(min(nums[i],nums[i+1]))
                    else:
                        new_nums.append(max(nums[i],nums[i+1]))
                return minmax(new_nums)
                
        return minmax(nums)
