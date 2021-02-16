# Used Levenshtein distance

from collections import defaultdict

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp, a, b = defaultdict(int), len(word1), len(word2)
        
        for j in range(len(word1) + 1):  # 첫행 및 첫열 값 
            dp[j,0] = j
        
        for i in range(len(word2) + 1):
            dp[0,i] = i

        for i in range(1, a+1): #나머지 행 추가
            for j in range(1, b+1):
                if word1[i-1] == word2[j-1]:
                    dp[i,j] = dp[i - 1, j - 1]
                else:
                    dp[i,j] = min(dp[i - 1,j], dp[i - 1,j - 1], dp[i,j - 1]) + 1


        return dp[a,b]
