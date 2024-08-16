class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        while True:
            nums.sort()
            if k == 0:
                print('done')
                break
            for i in range(len(nums)):
                if k == 0:

                    return sum(nums)
                elif nums[0] < 0:
                    nums[0] *= (-1)
                    k -= 1
                    nums.sort()

                elif nums[i] == 0:
                    k -= 1
                    nums.sort()
                else:
                    nums[0] *= (-1)
                    k -= 1
                    nums.sort()

        return sum(nums)
        
