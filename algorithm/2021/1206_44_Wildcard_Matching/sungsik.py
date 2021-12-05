class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic Programming
        dp = [[0] * (len(s)+1) for _ in range(len(p)+1)]
        
        # base case
        # s의 길이가 0이고 p의 길이가 0일 경우 1
        # s의 길이가 0이고 p가 앞에서부터 '*'가 연속되면 
        # 그 개수만큼 1로 설정
        # p의 길이가 0이고 s의 길이가 0이 아닐 경우는 0 -> 기본값이 0이므로 코드로 작성하진 않음
        dp[0][0] = 1
        for i in range(1, len(p)+1):
            if p[:i] == '*' * i:
                dp[i][0] = 1
            else:
                break
        
        # recursive equation
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                # 만약 p의 마지막이 '?'이거나
                # p의 마지막과 s의 마지막이 같을 경우는
                # 서로 끝을 제외한 경우의 수로 설정
                if p[i-1] == '?' or p[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 만약 p의 마지막이 '*'일 경우
                # 1. '*'을 empty string으로 볼 경우 -> dp[i-1][j]
                # 2. '*'을 empty string으로 보지 않을 경우 -> dp[i][1] + dp[i][2] + ... + dp[i][j-1]
                #    => j가 작을 때 부터 순회하고 크기가 중요하지 않으므로 dp[i][j-1]만 고려해도 문제 없음
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                # 위에 해당하지 않으면 0으로 설정 -> 기본값이 0이므로 코드로 작성하진 않음
        
        return dp[len(p)][len(s)] > 0
        
