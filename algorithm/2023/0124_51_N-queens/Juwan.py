
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [] 
        board = [['.' for _ in range(n)] for _ in range(n)]
        dia = set()
        col = set()
        def backtracking(i):
            if i==n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            for j in range(0,n):
                if j in col or valid(i,j) == False:
                    continue
                col.add(j)
                dia.add((i,j))
                board[i][j] = 'Q'
                backtracking(i+1)
                col.remove(j)
                dia.remove((i,j))
                board[i][j] = '.'
        
        def valid(i,j):
            for x,y in dia:
              
                if abs(x-i) == abs(y-j):
                    return False
                  
            return True

        backtracking(0)
        return ans
