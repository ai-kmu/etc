class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)     # 정렬
        return nums[k-1]            # k-1번째 리턴
