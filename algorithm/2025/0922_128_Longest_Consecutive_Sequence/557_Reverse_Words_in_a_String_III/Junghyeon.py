class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")

        result = ""

        for i in s:
            result += i[::-1]
            result += " "

        # print(result)

        return result.strip()
