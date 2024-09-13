class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        t = ""
        idx = 0
        if len(word1) >= len(word2):
            for i, c in enumerate(word2):
                t += word1[i]
                t += word2[i]
                idx = i
            t += word1[i+1:]
        else:
            for i, c in enumerate(word1):
                t += word1[i]
                t += word2[i]
                idx = i
            t += word2[i+1:]
        return t
