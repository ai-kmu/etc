class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        ans = ""
        flag = True
        while i < len(word1) or j < len(word2):
            try:
                if flag:
                    ans += word1[i]
                    i += 1
                else:
                    ans += word2[j]
                    j += 1
            except:
                pass
            flag = not flag
        return ans 
