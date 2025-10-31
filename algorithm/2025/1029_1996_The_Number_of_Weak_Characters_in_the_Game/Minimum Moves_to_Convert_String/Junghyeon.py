class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        pointer = 0

        while pointer < len(s):
            if s[pointer] == 'X':
                pointer += 3
                cnt +=1
            else:
                pointer += 1
        return cnt
