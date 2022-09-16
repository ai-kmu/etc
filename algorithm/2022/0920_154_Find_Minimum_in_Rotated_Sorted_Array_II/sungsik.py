class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 숫자가 작아지는 위치가 있다면 해당 값을 반환하고, 아니면 첫번째 숫자를 반환한다.
        return next((n for prev_n, n in zip(nums[:-1], nums[1:]) if prev_n > n), nums[0])
