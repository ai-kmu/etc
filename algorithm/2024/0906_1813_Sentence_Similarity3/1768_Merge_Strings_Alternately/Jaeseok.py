class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        l1, l2 = len(word1), len(word2)
        i, j = 0, 0
        first = min(l1, l2)
        second = max(l1, l2)
        while j < first:
            answer += word1[i]
            answer += word2[j]
            i += 1
            j += 1
        if l1 > l2:
            while i < second:
                answer += word1[i]
                i += 1
        else:
            while j < second:
                answer += word2[j]
                j += 1

        return answer
