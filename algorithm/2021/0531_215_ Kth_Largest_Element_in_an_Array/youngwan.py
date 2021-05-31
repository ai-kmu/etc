class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums, reverse=True)                 # 내림차순 정렬
        return nums_sorted[k-1]
