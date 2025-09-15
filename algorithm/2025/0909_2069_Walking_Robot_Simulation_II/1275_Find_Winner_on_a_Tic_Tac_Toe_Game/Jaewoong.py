from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        win = [
            [(0,0),(0,1),(0,2)],
            [(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],
            [(0,0),(1,0),(2,0)],
            [(0,1),(1,1),(2,1)],
            [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)],
            [(0,2),(1,1),(2,0)]
        ]

        move_A, move_B = [], []

        for i in range(len(moves)):
            if i % 2 == 0:
                move_A.append(tuple(moves[i]))
            else:
                move_B.append(tuple(moves[i]))

        set_A, set_B = set(move_A), set(move_B)

        for w in win:
            if set(w).issubset(set_A):
                return "A"
            if set(w).issubset(set_B):
                return "B"

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
