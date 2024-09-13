class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len2 = len(word2)

        answer = ''
        for i, s1 in enumerate(word1):
            # word2가 짧으면 중간에 끊기
            if i == len2:
                break
            s2 = word2[i]
            answer += s1 + s2
        
        # word2가 길면
        if (i + 1) < len2:
            answer += word2[i + 1:]
        # word2가 짧으면
        elif (i + 1) > len2:
            answer += word1[i:]
        
        return answer
