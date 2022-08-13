from collections import deque
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp 방식으로 풀이
        dp 배열 안 요소는 각 위치까지 생성할 수 있는 최대 길이 sequence를 말함
        '''
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                '''
                nums[i]가 nums[j]보다 클 경우(j < i) j 위치에서의 최대 길이 값의 +1 한것과
                현재 위치 i에서의 dp값 dp[i] 중 큰 것으로 dp[i] 값을 업데이트 한다.
                이러한 방법으로 i 위치에서의 최대 길이 값을 구현한다.
                그러기 위해서는 현재 위치에서의 nums값 보다 j 위치에서의 nums값이 작아야 한다.
                '''
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp) # 이 문제는 각 위치에서 봤을 때 최대 길이 값이므로 dp의 최대값을 출력
