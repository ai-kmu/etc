class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag_1 = 0
        diag_2 = 0
        current_player = 1

        for y, x in moves:
            rows[y] += current_player
            cols[x] += current_player
            if y == x:
                diag_1 += current_player
            if y + x == 2:
                diag_2 += current_player

            if abs(rows[y]) == 3 or abs(cols[x]) == 3 or abs(diag_1) == 3 or abs(diag_2) == 3:
                if current_player == 1:
                    return "A"
                else:
                    return "B"

            current_player = -current_player

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
