class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1s, p2s = 0, 0
        p1t, p2t = 0, 0
        for i in range(len(player1)):
            if p1t != 0:
                p1s += player1[i]
                p1s += player1[i]
            else:
                p1s += player1[i]

            if p2t != 0:
                p2s += player2[i]
                p2s += player2[i]
            else:
                p2s += player2[i]
            
            if player1[i] == 10:
                p1t = 2
            if player2[i] == 10:
                p2t = 2
            if player1[i] != 10 and p1t != 0:
                p1t -= 1
            if player2[i] != 10 and p2t != 0:
                p2t -= 1
        if p1s > p2s:
            return 1
        elif p1s < p2s:
            return 2
        else:
            return 0
