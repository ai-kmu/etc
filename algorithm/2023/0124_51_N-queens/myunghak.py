class Solution:
    def solveNQueens(self, n: int):
        cboard = [-1] * n
        result = []

        def is_correct(y, x):
            for i in range(y):
                if cboard[i] == x or abs(cboard[i] - x) == y - i:
                    return False
            return True
        
        def bt(y):
            if y == n:
                result.append([ "." * i + "Q" + "." * (n-i-1) for i in cboard])
                return
            
            for x in range(n):
                if is_correct(y, x):
                    cboard[y] = x
                    bt(y + 1)
                    cboard[y] = -1
        
        bt(0)
        return result
    
