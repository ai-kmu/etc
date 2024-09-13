class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        ans = ""
        while True:
            if idx == len(word1) or idx == len(word2):
                break
            ans += word1[idx]
            ans += word2[idx]
            idx += 1

        if idx == len(word1):
            ans += word2[idx:]
        else:
            ans += word1[idx:]
        
        return ans
