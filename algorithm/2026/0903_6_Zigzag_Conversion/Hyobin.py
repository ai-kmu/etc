class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        tmp = [[] for _ in range(numRows)]
        ans = ''
        row = 0
        direc = 1

        for i in range(len(s)):
            tmp[row].append(s[i])

            if row == 0:
                direc = 1
            elif row == numRows - 1:
                direc = -1
            
            row += direc
        
        for row in tmp:
            for char in row:
                ans += char

        return ans
