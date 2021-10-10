class Solution:
    # memoization을 활용한 풀이
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 합쳤을 때 최대가 되는 값
        # 최솟값은 -maximum
        maximum = sum([abs(x) for x in nums])
        # 각 index마다 현재까지의 sum이 특정 값일때의 결과를 기록하는 memo
        # 범위가 -maximum ~ +maximum이기 떄문에 2*maximum+1만큼의 공간 필요
        memo = [[-1 for _ in range(2*maximum+1)] for __ in range(len(nums))]
        
        def solve(index, tmp_sum):
            # 만약 index가 끝까지 돌았을 경우
            if index == len(nums):
                # target과 같은 경우 원하는 답이므로 1을 리턴
                if tmp_sum == target:
                    return 1
                return 0
            # 만약 memo가 적혀있지 않는 경우
            # memo의 범위가 0 ~ 2*maximum이므로 맞춰주기 위해 maximum만큼 더함
            if memo[index][tmp_sum+maximum] < 0:
                # 해당 위치와 값에서
                # 현재값을 더하고 뺀값을 재귀적으로 호출해서 구해서 이를 더함
                memo[index][tmp_sum+maximum] = solve(index+1, tmp_sum+nums[index]) + solve(index+1, tmp_sum-nums[index])
            return memo[index][tmp_sum+maximum]
        
        return solve(0, 0)
