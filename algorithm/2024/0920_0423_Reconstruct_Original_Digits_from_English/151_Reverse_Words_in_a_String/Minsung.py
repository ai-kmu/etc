class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        r_words = list()
        for i in words:
            if i=='': continue
            r_words.append(i)
        r_words = r_words[::-1]
        ans = ' '.join(r_words)
        return ans
