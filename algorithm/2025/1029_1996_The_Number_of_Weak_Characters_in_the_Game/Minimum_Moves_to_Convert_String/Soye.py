class Solution:
    def minimumMoves(self, s: str) -> int:
        tmp = list(s)
        ans = 0

        for i in range(len(tmp) - 2):
            if (i == len(tmp) - 3 and tmp[-3:].count('X') > 0):
                ans += 1
                break

            if(tmp[i] == 'X'):
                ans += 1
                tmp[i] = 'O'
                tmp[i + 1] = 'O'
                tmp[i + 2] = 'O'
    
        return ans

