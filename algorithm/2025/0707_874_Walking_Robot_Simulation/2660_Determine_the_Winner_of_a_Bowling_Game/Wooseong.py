class Solution:
    def calcul(self, array):
        strike = 0
        total = 0
        for pin in array:
            total += pin
            if strike:
                total += pin
                strike -= 1
            if pin == 10:
                strike = 2
        return total

    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1 = self.calcul(player1)
        score2 = self.calcul(player2)
        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        else:
            return 0
