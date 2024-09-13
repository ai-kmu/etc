class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        flag = True
        result = ''

        while True:
            if i == len(word1) or j == len(word2):
                break
            else:
                if flag:
                    result += word1[i]
                    i += 1
                    flag = False
                else:
                    result += word2[j]
                    j += 1
                    flag = True
                    
        if i == len(word1):
            result += word2[j:]
        if j == len(word2):
            result += word1[i:]
            
        return result
