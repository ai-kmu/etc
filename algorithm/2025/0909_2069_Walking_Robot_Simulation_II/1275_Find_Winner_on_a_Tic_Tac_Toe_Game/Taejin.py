class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        win = "Draw"
        a_moves = moves[::2]
        b_moves = moves[1::2]
        grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]
        
        for a_x, a_y in a_moves:
            grid[a_x][a_y] = 1
        for b_x, b_y in b_moves:
            grid[b_x][b_y] = -1

        for i in range(3):
            if (sum(grid[i]) == 3) or (sum(grid[j][i] for j in range(3)) == 3):
                win = "A"
                break
            
            elif (sum(grid[i]) == -3) or (sum(grid[j][i] for j in range(3)) == -3):
                win = "B"
                break

        if (sum([grid[i][i] for i in range(3)]) == 3) or (sum([grid[2 - i][i] for i in range(3)]) == 3):
            win = "A"

        elif (sum([grid[i][i] for i in range(3)]) == -3) or (sum([grid[2 - i][i] for i in range(3)]) == -3):
            win = "B"

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0 and win == "Draw":
                    win = "Pending"

        return win
