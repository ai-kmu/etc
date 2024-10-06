class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        dp 이용
            - dp[i]: 3으로 나누었을 때, 나머지가 i인 수 중 가장 큰 수 저장
        '''
        dp = [0] * 3

        for i in nums:
            remainder = i % 3  # 현재 수의 3으로 나누었을 때의 나머지 
            from copy import deepcopy
            copied_dp = deepcopy(dp)  # 현재 수의 중복 계산 방지

            for idx in range(3):
                if remainder == 0:  # 0 -> 어느 index든 상관 없음
                    dp[idx] += i
                elif remainder == 1:
                    if copied_dp[(idx-1+3)%3] % 3 == (idx-1+3)%3:  # 실제로 유효한 나머지를 가지는 지 확인
                        dp[idx] = max(copied_dp[idx], copied_dp[(idx-1+3)%3] + i)
                elif remainder == 2:
                    if copied_dp[(idx-2+3)%3] % 3 == (idx-2+3)%3:  # 실제로 유효한 나머지를 가지는 지 확인
                        dp[idx] = max(copied_dp[idx], copied_dp[(idx-2+3)%3] + i)

        return dp[0]  
