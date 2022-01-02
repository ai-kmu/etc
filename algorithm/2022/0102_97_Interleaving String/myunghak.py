# DP로 품
# s1과 s2를 각각 가로축 세로축으로 만든 행렬을 dp라 두었을 때
# dp[:l][:k]는 s1[:l]과 s2[:k]으로 s3[:l+k]를 만들 수 있는지 저장



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        
        if len(s1) + len(s2) != len(s3):
            return False
        

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1)+1)]
        
        # 우선 3다 아무것도 없으면 True
        dp[0][0] = True

        # s1과 s2 각각 따로 생각 했을 때를 초기화
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for i in range(1, len(s2) + 1):
            dp[0][i] = dp[0][i - 1] and s2[i - 1] == s3[i - 1]

            
        # 새로 추가되는애가 남은것의 첫번째와 같으면 True 아니면 False
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] += (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                dp[i][j] += (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1] > 0
