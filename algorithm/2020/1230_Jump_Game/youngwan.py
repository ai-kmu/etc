class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        for idx, num in enumerate(nums[:-1]):
            if num == 0:                                  # jump 숫자가 0인 경우
                if pos <= idx:                            # 갈 수 있는 곳이 현재 온 곳보다 작거나 같다면
                    return False                          # False를 반환
                else:                                     # 갈 수 있는 곳이 현재 온 곳보다 더 크다면
                    continue                              # 다음으로 넘어감
            pos = num+idx if pos < num+idx else pos       # 최대 갈 수 있는 곳은 (현재 위치 + jump 숫자)와 (pos) 값 중 큰 값
        return True if pos >= len(nums) - 1 else False    # pos 값이 마지막 위치보다 크거나 같다면 True 반환
