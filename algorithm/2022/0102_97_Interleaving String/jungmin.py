class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        # dp 2d array 생성. 생성할 때 인덱스가 1번째는 문자열에서의 첫번째를 가리키도록 각 s길이 + 1만큼 [0] array 생성
        dp = [0] * (len(s1)+1)

        for i in range(len(s1)+1):
            dp[i] = [0] * (len(s2)+1)
        
        # dp를 이용하여 구현
        # s1에서 하나씩 뽑을 때와 s2에서 하나씩 뽑을 때를 고려하여 dp 계산
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0: # dp의 0번째 행과 0번째 열에는 1을 저장
                    dp[i][j] = 1

                elif i == 0: # 0번째 행에서 1번째 열부터는 이전 열에서의 값이 1이고 현재 s2문자가 s3의 i+j-1 인덱스에서의 문자와 같은 경우 1로 저장. 조건에 맞지 않으면 0으로 저장
                    dp[i][j] = (1 if dp[i][j-1] and s2[j-1] == s3[i+j-1] else 0)

                elif j == 0: # 0번째 열에서는 이전 행에서의 값이 1이고 현재 s1문자가 s3의 i+j-1 인덱스에서의 문자와 같은 경우 1로 저장. 조건에 맞지 않으면 0으로 저장
                    dp[i][j] = (1 if dp[i-1][j] and s1[i-1] == s3[i+j-1] else 0)

                else: # 그 외엔 elif 두가지 중 하나라도 충족하는 경우 1로 저장.  그렇지 않으면 0으로 저장
                    dp[i][j] = 1 if (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]) else 0
        return dp[len(s1)][len(s2)] # dp를 계산하여 dp의 마지막 행과 열의 값을 출력함
