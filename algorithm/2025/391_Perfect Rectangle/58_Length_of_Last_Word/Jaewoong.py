class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        for i in s:
            if i != ' ':
                word += i
            else:
                if len(word) > 0:
                    last = word
                word = ""
        if len(word) > 0:
            last = word

        return len(last)
