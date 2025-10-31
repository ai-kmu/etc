class Solution:
    def minimumMoves(self, s: str) -> int:
        i = 0
        cnt = 0

        while i < len(s):
            if s[i] == 'X':
                cnt += 1
                i += 3

            else:
                i += 1

        return cnt
