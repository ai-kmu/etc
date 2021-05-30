class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #배열을 역으로 정렬한 뒤 k번째의 숫자를 뽑는다.
        return sorted(nums, reverse=True)[k-1]
