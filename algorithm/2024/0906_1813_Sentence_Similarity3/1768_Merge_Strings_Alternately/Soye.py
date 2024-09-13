class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for idx in range(len(word1)):
            ans = ans + word1[idx]
            if idx < len(word2):
                ans = ans + word2[idx]


        if len(word1) < len(word2):
            for idx in range(len(word1), len(word2)):
                ans = ans + word2[idx]

        return ans
