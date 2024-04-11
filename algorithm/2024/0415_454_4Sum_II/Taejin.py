from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums12 = defaultdict(int)
        nums34 = defaultdict(int)
        
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                nums12[-(nums1[i] + nums2[j])] += 1
                nums34[nums3[i] + nums4[j]] += 1

        ret = 0
        for k in nums12.keys():
            ret += (nums12[k] * nums34[k])

        return ret
        
