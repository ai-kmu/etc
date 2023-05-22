# 답보고 풀었어요

# Sliding window 방식입니다.
# sliding window의 크기는 0에서 시작해서 max(=answer)값까지 커지고 그 크기를 유지하게 됩니다.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1
