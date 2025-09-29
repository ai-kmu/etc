class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        word = []
        for i in s:
            if i != ' ':
                word.append(i)

            if i == ' ':
                words.append(word)
                word = []
                words.append(' ')
        words.append(word)
        ans = ''
        for w in words:
            for j in list(reversed(w)):
                ans += j
                
        return str(ans)

