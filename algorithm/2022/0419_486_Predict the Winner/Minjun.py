'''
1번 선수의 점수가 2번 선수보다 크거나 같도록 할 수 있는가? 문제
dp 문제
2번 선수 또한 매번 최적의 선택을 한 경우에 1번 선수 승리 여부를 알 수 있다.
1번 선수와 2번 선수의 총합 차이 비교
'''

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        # nums 길이가 1 이거나,
        # nums 길이가 짝수라면 
        # 내가 선택우선권을 갖기 때문에 반드시 승리할 수 있다.
        if n == 1 or n % 2 == 0:
            return True
        
        # 선택마다의 점수 차이를 담을 2차원 dp 선언
        dp = [[0]*n for i in range(n)]
        
        # dp배열에서 시작(대각성분)은 내가 고른 값.
        for i in range(n):
            dp[i][i] = nums[i]
        
        # 대각선으로 값 비교해나간다.
        for d in range(1,n):
            # 대각선 성분 개수
            for i in range(n-d):
                
                j = i + d
                
                # 앞 뒤 최적의 선택을 비교해서 담는다
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        
        # 점수 차이가 0이거나 양수면 1번 선수가 승리 True 반환
        return dp[0][n-1] >= 0
        
