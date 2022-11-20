class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 진짜 모르겠음... 
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
