class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # print(word1[0])
        answer = ''
        w_1_len = len(word1)
        w_2_len = len(word2)
        for i in range(max(w_2_len,w_1_len)):
            if i < w_1_len:
                answer +=  word1[i]
            if i < w_2_len:
                answer +=  word2[i]

        return answer
