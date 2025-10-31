class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        n = len(s)

        skip_flag = 0
        
        for i in range(n):
            if i < skip_flag:
                continue

            if s[i] == 'X':
                cnt += 1
                skip_flag = i + 3
        
        return cnt
