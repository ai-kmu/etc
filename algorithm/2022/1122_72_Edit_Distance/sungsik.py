# dp로 풀어보려다 실패..

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i
        for i in range(1, n+1):
            dp[0][i] = i
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                val = -1
                upper = dp[i-1][j]
                left = dp[i][j-1]
                lower = min(upper, left)
                if word1[i-1] == word2[j-1]:
                    if i == j:
                        val = lower
                        if not (i > 2 and j > 2 and (word1[i-2] == word2[j-1] or word1[i-1] == word2[j-1])):
                            val -= 1
                    else:
                        val = lower
                else:
                    if i == j:
                        val = lower
                    else:
                        val = lower + 1
                dp[i][j] = val
        
        for row in dp:
            print(row)
        return dp[m][n]
