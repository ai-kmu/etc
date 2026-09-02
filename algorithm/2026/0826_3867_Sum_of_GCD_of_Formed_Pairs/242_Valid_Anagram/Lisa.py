class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            index = ord(ch) - ord('a')
            count[index] -= 1

            if count[index] < 0:
                return False

        return True