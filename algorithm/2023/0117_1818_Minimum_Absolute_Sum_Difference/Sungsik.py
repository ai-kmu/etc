from bisect import bisect

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        n = len(nums1)

        diff_nums = [abs(x - y) for x, y in zip(nums1, nums2)]

        min_diff = sum(diff_nums)
        tmp_min_diff = min_diff

        for i, diff in enumerate(diff_nums):
            num2 = nums2[i]
            similar_idx = bisect(sorted_nums1, num2)
            if 0 < similar_idx <= n-1:
                closest_diff = min(abs(num2 - sorted_nums1[similar_idx-1]), abs(num2 - sorted_nums1[similar_idx]))
            elif similar_idx == 0:
                closest_diff = abs(num2 - sorted_nums1[similar_idx])
            else:
                closest_diff = abs(num2 - sorted_nums1[similar_idx-1])

            tmp_min_diff = min(tmp_min_diff, min_diff-diff+closest_diff)

        return tmp_min_diff % (10 ** 9 + 7)
