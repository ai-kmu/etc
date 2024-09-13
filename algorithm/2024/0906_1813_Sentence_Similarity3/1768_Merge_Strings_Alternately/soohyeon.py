class Solution(object):
    def mergeAlternately(self, word1, word2):
    
        result = ""
        j = 0

        if len(word1) < len(word2):
            for i in range(len(word1)):
                result += word1[i] + word2[i]
                j+= 1
            result += word2[j:]
        else:
            for i in range(len(word2)):
                result += word1[i] + word2[i]
                j+= 1
            result += word1[j:]

        return result