from bisect import bisect_right

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        if nums1 == nums2:
            return 0

        temp = sorted(nums1)
        
        n = len(nums1)

        ans = 0

        max_diff = float('-inf')
        
        for idx, (i, j) in enumerate(list(zip(nums1, nums2))):
            
            diff = abs(i-j)

            ans += diff

            c_i = bisect_right(temp, j) - 1

            a = abs(temp[c_i] - j)
            b = None

            if c_i + 1 < n:
                b = abs(temp[c_i + 1]-j)

            max_diff = max(diff-a, diff-b if b else 0, max_diff)

        return (ans - max_diff) % (10 ** 9 + 7)
