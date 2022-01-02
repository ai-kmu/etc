class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        
        if (m + n) != len(s3):
            return False
        
        S = [[False] * (n+1) for _ in range(m+1)]
        
        S[0][0] = True
        for i in range(1, m+1):
            if s1[i-1] == s3[i-1]:
                S[i][0] = True
            else:
                break
        for i in range(1, n+1):
            if s2[i-1] == s3[i-1]:
                S[0][i] = True
            else:
                break
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                S[i][j] |= (s1[i-1] == s3[i+j-1] and S[i-1][j])
                S[i][j] |= (s2[j-1] == s3[i+j-1] and S[i][j-1])
        
        return S[m][n]
