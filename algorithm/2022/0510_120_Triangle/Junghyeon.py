import copy


class Solution:
    '''
    dp -> top down 방식으로 업데이트
    '''
    def minimumTotal(self, triangle):
        # 입력값인 triangle 배열을 깊은 복사를 통해 dp 테이블을 만든다.
        dp = copy.deepcopy(triangle)
        
        for i in range(len(triangle)-1):
            dp[i+1][0] += dp[i][0]
            for j in range(i):
                # 더 작은 값을 업데이트
                dp[i+1][j+1] += min((dp[i][j+1], dp[i][j]))
            dp[i+1][-1] += dp[i][-1]
            
        return min(dp[-1])
