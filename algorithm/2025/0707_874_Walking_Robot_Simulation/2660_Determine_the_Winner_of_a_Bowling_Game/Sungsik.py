class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score = lambda lst: sum([s * 2 if (i >= 1 and lst[i-1] == 10) or (i >= 2 and lst[i-2] == 10) else s for i, s in enumerate(lst)])
        score1, score2 = score(player1), score(player2)
        return 1 if score1 > score2 else 2 if score1 < score2 else 0
