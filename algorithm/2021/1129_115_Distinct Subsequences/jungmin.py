class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 가로로 s길이, 세로로 t의 길이만큼의 2차원 리스트 dp를 생성
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]
        
        # t에서의 빈 string과 s를 비교했을 때 s에 모두 포함하므로 0번째 행은 1로 다 저장
        for i in range(len(s)+1):
            dp[0][i] = 1
        
        for i in range(len(t)):
            for j in range(len(s)):
                # t에서 마지막 문자와 s에서 마지막 문자랑 같으면 현재 행에서 이전 값과 이전 행에서의 왼쪽위 대각선 값을 더함
                # 예: s에서의 "rabb"와 t에서 "rab"인 경우 -  t가 "ra"였을 때 s가 "rab"인 경우의 수와 t에서 "rab"일 때 s에서 "rab"인 경우를 더하면 된다.
                # 즉, 이전 t 행에 저장했던 값을 다시 불러와 추가하여 저장한다.
                if t[i] == s[j]: 
                    dp[i+1][j+1] =  dp[i][j] + dp[i+1][j]
                
                # t에서 마지막 문자와 s에서 마지막 문자랑 같지 않을 경우 현재 행에서 이전 값만 이어서 저장
                else:
                    dp[i+1][j+1] = dp[i+1][j]
                    
        return dp[-1][-1] # dynamic programming 방식으로 2차원 배열을 순차적으로 저장하여 최종값 출력
