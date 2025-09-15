class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        cnt = [[0]*8 for _ in range(2)]
        # 0-2 / 3-5 / 6-8
        # 0, 3, 6 / 1, 4, 7 / 2, 5, 8
        # 0, 4, 8 / 2, 4, 6
        
        playerA = True
        for i, j in moves:
            p = 0 if playerA else 1

            touched = [i, 3 + j]
            if i == j:
                touched.append(6)
            if i + j == 2:
                touched.append(7)

            for idx in touched:
                cnt[p][idx] += 1
                if cnt[p][idx] == 3:
                    return "AB"[p]

            playerA = not playerA

        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"
