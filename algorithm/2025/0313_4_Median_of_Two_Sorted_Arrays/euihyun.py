class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # O(log (m+n))는 어케 푸노?..
      
        ans = 0
        nums = (nums1+nums2)
        nums.sort()
        #걍 median 구했음~
        if len(nums) % 2 == 0:
            flag = len(nums) // 2             
            ans = float((nums[flag] + nums[flag-1]) / 2.0)
        else:
            flag = len(nums) // 2 
            ans = (nums[flag])


        return ans
