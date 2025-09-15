class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wins = \
        [
            {(0, 0), (0, 1), (0, 2)}, 
            {(1, 0), (1, 1), (1, 2)}, 
            {(2, 0), (2, 1), (2, 2)}, 
            {(0, 0), (1, 0), (2, 0)}, 
            {(0, 1), (1, 1), (2, 1)}, 
            {(0, 2), (1, 2), (2, 2)}, 
            {(0, 0), (1, 1), (2, 2)}, 
            {(1, 1), (0, 2), (2, 0)}
        ]
        
        A = []
        B = []

        for i in range(0, len(moves), 2):
            A.append(moves[i])
            if i + 1 < len(moves):
                B.append(moves[i + 1])
        
        set_A = set()
        for a in A:
            set_A.add(tuple(a))

        set_B = set()
        for b in B:
            set_B.add(tuple(b))
        
        # print(set_A)

        for win_set in wins:
            if win_set <= set_A:
                return "A"
            if win_set <= set_B:
                return "B"

        if len(moves) == 9:
            return "Draw"
        
        else:
            return "Pending"
        
