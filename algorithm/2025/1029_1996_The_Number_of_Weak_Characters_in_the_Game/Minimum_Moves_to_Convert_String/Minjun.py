class Solution:
    def minimumMoves(self, s: str) -> int:
        tmp = 0
        cnt = 0
        for i, c in enumerate(s):
            if c == 'O':
                if tmp > 0:
                    tmp -= 1
                continue
            if tmp == 0:
                tmp = 2
                cnt += 1
                continue
            tmp -= 1
        return cnt
