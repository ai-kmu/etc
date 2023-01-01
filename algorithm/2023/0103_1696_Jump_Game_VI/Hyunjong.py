# time limit error
class Solution(object):
    def maxResult(self, nums, k):
        # dp 사용
        # 0으로 초기화
        dp = [0 for i in range(len(nums))]
        
        # dp에 첫번째 값, 두번째 값 입력
        dp[0] = nums[0]
        dp[1] = nums[0] + nums[1]

        # 2 index부터 모든 dp에 대해 반복
        for i in range(2, len(nums)):
            # max값 선언
            max_val = -100000000000000000
            
            # 매 dp i 마다 가능한 step을 조사하여 최대값 추출
            for j in range(1, k+1):
                # 0보다 작으면 out of boundary
                if i-j >= 0:
                    # 최대값 추출
                    max_val = max(max_val, dp[i-j])
            # dp를 가장 큰 값으로 업데이트
            dp[i] = max_val + nums[i]
        return dp[-1]
