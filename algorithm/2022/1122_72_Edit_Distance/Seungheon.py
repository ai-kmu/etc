
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # i번째 까지의 단어를 j 번째 까지의 단어로 바꾸는 최소의 횟수로 dp update
       
        # 예외처리 
        if not word1 or not word2:
            return max(len(word1), len(word2))
        
        dp = [ [0 for _ in word1] for _ in word2]
        
        # 0,0 initialization
        dp[0][0] = 0 if word1[0] == word2[0] else 1
        
        # first row initialization
        flag = 0
        for i in range(1, len(word1)):
            dp[0][i] = dp[0][i-1] if word2[0] == word1[i] and flag == 0 else dp[0][i-1] + 1
            if word2[0] == word1[i]:
                flag = 1
            
        # first col initialization
        flag = 1 if word1[0] == word2[0] else 0
        for i in range(1, len(word2)):
            dp[i][0] = dp[i-1][0] if word1[0] == word2[i] and flag == 0 else dp[i-1][0] + 1
            if word2[i] == word1[0]:
                flag = 1

        # dp 채우기
        for i in range(1, len(word2)):
            for j in range(1, len(word1)):
                
                # 같은 char일 경우 해당하는 char를 사용하지 않음
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i-1][j-1]
                # 같은 char이 아닌경우 이 전 단계의 최솟값 + 1을 함
                else:
                    tmp_min = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    dp[i][j] = tmp_min + 1

        return dp[-1][-1]
