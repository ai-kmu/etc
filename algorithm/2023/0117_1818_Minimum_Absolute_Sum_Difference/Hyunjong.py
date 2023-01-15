# brute force => time limit exceeded
class Solution:
  def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        diff_list = []
        # 기존 diff 값을 구한다.
        for i in range(n):
            diff_list.append(abs(nums1[i] - nums2[i]))
        diff = sum(diff_list)

        min_diff = diff
        # 전체 탐색
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # diff - diff[i] + 바꾼 diff[i]
                new_diff = diff - diff_list[i] + abs(nums1[j] - nums2[i])
                min_diff = min(min_diff, new_diff)
        return min_diff % (10**9 + 7)
