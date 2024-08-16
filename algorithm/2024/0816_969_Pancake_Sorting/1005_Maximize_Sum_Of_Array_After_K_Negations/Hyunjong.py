class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k != 0:
            # sort
            nums = sorted(nums)
            # 만약 가장 작은 수가 음수면 양수로 바꾸기
            if nums[0] < 0:
                nums[0] = -nums[0]
            # 가장 작은 수가 0이거나 양수면
            else:
                # k가 짝수이면, 두번 적용하면 됨
                if k % 2 == 0:
                    k -= 2
                    break
                # 아니면 가장 작은거 음수로
                else:
                    nums[0] = -nums[0]
                    break
            # k 돌리기
            k -= 1
        # 다 더하기
        return sum(nums)
