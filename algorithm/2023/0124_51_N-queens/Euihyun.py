class Solution(object):
    def solveNQueens(self, n):
        board = [['.']*n for i in range(n)]
        ans =[]
        def issafe(r,c):
            n = len(board)
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
                if  c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                if  c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True
                
        def solve(r):
            n = len(board)
            if r == n:
                ans.append(["".join(i) for i in board])
                return
            for c in range(n):
                if issafe(r,c):
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'

        solve(0)
        return ans

        
        
