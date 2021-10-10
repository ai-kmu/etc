class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # +, -는 어디든 배치 가능
        # dp 사용
        # 모든 경우의 수 탐색
        
        answer = {}
        
        # index와 sum을 인자로 넣어주는 dfs를 재귀적으로 호출
        def dfs(idx, t_sum):
            if idx == len(nums):
                return t_sum == target

            if (idx, t_sum) in answer:
                return answer[(idx, t_sum)]
            
            # 하나하나 dfs로 +, - 경우 다 탐색
            answer[(idx, t_sum)] = dfs(idx+1, t_sum+nums[idx]) + \
                              dfs(idx+1, t_sum-nums[idx])

            return answer[(idx, t_sum)]

        return dfs(0, 0)
