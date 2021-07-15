class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range (m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.is_answer(i,j,board , word[1:]):
                        return True

        return False

    def is_answer(self, i, j, board , word):
        if len(word) == 0:
            return True

        w = word[0]
        tmp = board[i][j]
        ans = False
        board[i][j] = "0"

        if i + 1 < len(board) and board[i + 1][j] == w:
            ans = ans or self.is_answer(i + 1, j, board, word[1:])
        if i - 1 > -1 and board[i - 1][j] == w:
            ans = ans or self.is_answer(i - 1, j, board ,  word[1:])
        if j + 1 < len(board[0]) and board[i][j + 1] == w:
            ans = ans or self.is_answer(i, j + 1, board , word[1:])
        if j - 1 > -1 and board[i][j - 1] == w:
            ans = ans or self.is_answer(i, j - 1, board , word[1:])

        board[i][j] = tmp
        return ans
