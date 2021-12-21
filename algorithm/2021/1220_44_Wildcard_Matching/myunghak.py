# dp로 품
# *를 처리하는 것이 관건
# *를 처리할 때 *이후에 처음 matching되는 글자부터인지 아니면 
# 두번째 이후인지의 경우의 수를 dp로 처리
# dp의 구조는 dp[i][j] 가 True일 시 s[:i]와 p[:i]는 참이라는 것

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp 테이블 만듦, 우선 서로 아무것도 없는 경우는 당연히 True
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] != '*':
                break
            dp[0][i] = True
        
        for s_idx in range(1, len(s)+1):
            for p_idx in range(1, len(p)+1):
                if p[p_idx-1] == '*': # 현재 값이 *이면 이전 값을 보고 이전값이 True이면 현재도 같음 그러나 이전이 False이면 한칸 전의 값에 종속적
                    dp[s_idx][p_idx] = (dp[s_idx-1][p_idx] or dp[s_idx][p_idx-1])
                elif p[p_idx - 1] == s[s_idx - 1] or p[p_idx - 1] == '?': # 한칸 무시
                    dp[s_idx][p_idx] = dp[s_idx-1][p_idx-1]
                    
        return dp[-1][-1]
