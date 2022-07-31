class Solution(object):
# 슬라이딩 윈도우를 한칸씩 옮기면서 max값 추출
# 시간 초과
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        for i, _ in enumerate(nums):
            if len(nums) >= i + k:
                ans.append(max(nums[i: i+k]))
        return ans
