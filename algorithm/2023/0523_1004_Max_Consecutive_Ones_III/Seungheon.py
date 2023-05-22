class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 두개의 포인터 l, r를 이용
        l = 0
        for r in range(len(nums)):
            # k가 0이면, 바꿀 수 있는 0의 개수 감소
            if nums[r] == 0:
                k -= 1
            # 바꿀 수 있는 0의 개수가 감소하면
            if k < 0:
                # 끝에 있는값이 0인지 확인 하고 0이면, 바꿀 수 있는 0의 개수를 증가
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1


