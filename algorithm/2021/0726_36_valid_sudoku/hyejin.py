class Solution:
    def check_box(self, r, c, board):
        digits = [False for _ in range(9)]
        for i in range(r, r+3):
            for j in range(c, c+3):
                if board[i][j] == ".":
                    continue
                if digits[int(board[i][j])-1]:
                    return False
                digits[int(board[i][j])-1] = True
        return True
    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3x3 box안에 있는 숫자들이 유효한 경우인가
        check = True
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                check = self.check_box(r, c, board)
                if check is False:
                    return False
        
        
        row_check = [[False for _ in range(9)] for _ in range(9)]
        col_check = [[False for _ in range(9)] for _ in range(9)]
        # row에 있는 숫자들이 유효한가
        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == ".":
                    continue
                # row check
                if row_check[r][int(board[r][c])-1]:
                    return False
                row_check[r][int(board[r][c])-1] = True
        # column에 있는 숫자들이 유효한가 
        for r in range(0, 9):
            for c in range(0, 9):
                if board[c][r] == ".":
                    continue
                print(c, r, int(board[c][r]))
                if col_check[r][int(board[c][r])-1]:
                    return False
                col_check[r][int(board[c][r])-1] = True
                
        return True
        
