'''
솔루션 봤슴
'''
class Solution:
    def canPartitionKSubsets(nums, k):
    # 배열의 총합 계산
    tot = sum(nums)
    # 총합이 k로 나누어 떨어지지 않으면 False
    if tot % k:
        return False
    
    # 각 부분집합의 목표 합
    target = tot // k

    # 각 부분집합의 현재 합계 추적
    visited = [0] * k

    nums.sort(reverse=True)

    def recursion(i):
        # 모든 요소가 처리되었으면 True
        if i == len(nums):
            return True

        # k개의 부분집합 각각에 대해 시도
        for j in range(k):
            # 현재 부분집합에 nums[i]를 추가할 수 있는 경우
            if visited[j] + nums[i] <= target:
                visited[j] += nums[i]

                # 다음 요소에 대해 재귀적으로 탐색
                if recursion(i + 1):
                    return True

                # nums[i]를 추가하는 것이 해결책으로 이어지지 않으면 이전 상태로 되돌림
                visited[j] -= nums[i]

                # 현재 부분집합이 비어있다면 더 이상 다른 부분집합을 시도하지 않고 반복문을 종료
                if visited[j] == 0:
                    break
        return False

    # 재귀 함수 시작
    return recursion(0)
