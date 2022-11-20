# 실패 
# lcs을 찾고 그 이후에 어떻게 해야할지 모르겠음 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def printLCS(m,  n):
            if m == 0 or n == 0:
                return
            
            if S[m][n] == 0:
                printLCS(m-1, n-1)
                print(word1[m-1], end='')
            elif S[m][n] == 1:
                printLCS(m, n-1)
            elif S[m][n] == 2:
                printLCS(m-1, n)

        

        m = len(word1)
        n = len(word2)
        
        L = [[-1] * (n + 1) for item in range(m + 1)]
        S = [[0] * (n + 1) for item in range(m + 1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    L[i][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    L[i][j] = L[i-1][j-1]+1;
                    S[i][j] = 0
                else:
                    L[i][j] = max(L[i][j-1], L[i-1][j])
                    if L[i][j] == L[i][j-1]:
                        S[i][j] = 1
                    else:
                        S[i][j] = 2
        
        printLCS(m,  n)

        
