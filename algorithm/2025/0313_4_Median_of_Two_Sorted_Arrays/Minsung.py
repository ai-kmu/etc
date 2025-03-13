class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        median_pointer = None
        concat_nums = list()
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                concat_nums.append(nums1[i])
                i += 1
            else:
                concat_nums.append(nums2[j])
                j += 1
        while i<len(nums1):
            concat_nums.append(nums1[i])
            i+=1
        while j<len(nums2):
            concat_nums.append(nums2[j])
            j+=1
            
        if (len(nums1)+len(nums2))%2 == 1:
            return concat_nums[(len(nums1)+len(nums2))//2]
        else:
            return (concat_nums[(len(nums1)+len(nums2))//2]+concat_nums[(len(nums1)+len(nums2))//2-1])/2
