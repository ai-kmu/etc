class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabet_s = [0] * 26
        alphabet_t = [0] * 26

        for i in range(len(s)):
            alphabet_s[ord(s[i]) - 97] += 1
            alphabet_t[ord(t[i]) - 97] += 1

        return alphabet_s == alphabet_t
