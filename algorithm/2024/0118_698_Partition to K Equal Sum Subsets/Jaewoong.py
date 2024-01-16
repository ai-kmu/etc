# 정답보고 공부했습니다...
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)

        # 전체 합이 k로 나누어 떨어지지 않으면 불가능
        if total_sum % k != 0:
            return False

        target_sum = total_sum // k
        subsets = [0] * k

        def backtrack(index):
            # 모든 숫자를 다 사용했을 때, 각 부분 집합의 합이 목표값과 일치하는지 확인
            if index == len(nums):
                return all(subset == target_sum for subset in subsets)

            # 각 부분 집합에 현재 숫자를 넣어보며 탐색
            for i in range(k):
                if subsets[i] + nums[index] <= target_sum:
                    subsets[i] += nums[index]
                    # 재귀 호출로 다음 숫자를 처리
                    if backtrack(index + 1):
                        return True
                    subsets[i] -= nums[index]

                    # 최적화: 현재 숫자를 넣지 않고 다음 부분 집합으로 이동
                    if subsets[i] == 0:
                        break

            return False

        # 백트래킹을 시작하는 지점
        return backtrack(0)
