class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split(' ')
        result = ''

        for i in range(len(s_split)-1, -1, -1):
            if s_split[i] == "":
                continue
            else:
                result += s_split[i]
                result += " "

        return result[:-1]
