class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score = [0, 0, 0]
        n = len(player1)

        for i in range(n):
            if (i >= 1 and player1[i - 1] == 10) or (i >= 2 and player1[i - 2] == 10):
                score[1] += 2 * player1[i]
            else:
                score[1] += player1[i]

            if (i >= 1 and player2[i - 1] == 10) or (i >= 2 and player2[i - 2] == 10):
                score[2] += 2 * player2[i]
            else:
                score[2] += player2[i]

        if score[1] == score[2]:
            return 0
        elif score[1] > score[2]:
            return 1
        else: return 2
