class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            for i in range(len(word1) - len(word2)):
                word2 = word2 + str('0')
        elif len(word1) < len(word2):
            for i in range(len(word2) - len(word1)):
                word1 = word1 + str('0')

        output = ''
        for i in range(len(word1)):
            output = output + (word1[i] + word2[i])
        
        output = output.replace('0', '')

        return output
