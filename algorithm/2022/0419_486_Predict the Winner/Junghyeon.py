class Solution:
    def PredictTheWinner(self, nums):
        '''
        greedy로 시도했지만 실패 -> dp로 접근
        '''
        # nums의 길이만큼 정사각형 모양의 dp 테이블 생성
        dp = [[0] * (len(nums)) for _ in range(len(nums))]
        
        # 대각선의 원소를 우선 nums로 채운다.
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        
        # p1과 p2의 점수의 차이를 계산하면서 dp 테이블을 채워 나간다.
        for j in range(len(nums), 0, -1):
            for k in range(j, len(nums)):
                dp[j-1][k] = max(nums[k] - dp[j-1][k-1], nums[j-1] - dp[j][k])
                
        # dp[0][-1]에 저장되는 값 >= 0, p1의 승리
        if dp[0][-1] >= 0:
            return True
        else:
            return False
