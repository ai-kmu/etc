class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp 테이블 초기화
        dp = [1 for _ in range(n)]
        # subsequence를 만들고 뒤에서부터 탐색
        for i in range(n):
            # 증가하는 subsequence의 원소의 개수를 세는 변수
            count = 0
            # 앞에서부터 i번째 원소까지 가능한 increasing subsequence 탐색
            for j in range(i):
                # 만약에 i번째 원소가 j번째 원소보다 커서 increasing subsequence를 만족하면
                if nums[i] > nums[j]:
                    # 그 숫자까지 만들 수 있던 sequence 길이 중에 가장 큰 값을 count로 설정
                    count = max(count, dp[j])
            
            # i번째의 dp는 count에서 1을 더한 값
            dp[i] = count + 1
            
        return max(dp)
