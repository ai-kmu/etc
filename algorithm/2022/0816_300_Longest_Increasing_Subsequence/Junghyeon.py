class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp 테이블을 만들고 맨 끝 인덱스부터 가질 수 있는 최대의 길이를 저장
        '''
        # dp 테이블을 최솟값인 1로 초기화
        dp = [1] * len(nums)
        
        # 맨 끝 인덱스부터 탐색
        for i in range(len(dp)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
