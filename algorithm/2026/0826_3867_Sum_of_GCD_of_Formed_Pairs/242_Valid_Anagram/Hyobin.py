class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        tmp = [0] * 26

        for i in range(len(s)):
            tmp[ord(s[i]) - ord('a')] += 1
            tmp[ord(t[i]) - ord('a')] -= 1

        for c in tmp:
            if c != 0:
                return False

        return True
