
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        if len(player1) == 1 or len(player2) == 1:
            if player1[0] > player2[0]:
                return 1
            elif player1[0] < player2[0]:
                return 2
            else:
                return 0
        
        sum1, sum2 = 0, 0
        if len(player1) < 3 or len(player2) < 3:
            if player2[0] == 10:
                sum2 += player2[0] + 2 * player2[1]
            else:
                sum2 += player2[0] + player2[1] 
            if player1[0] == 10:
                sum1 += player1[0] + 2 * player1[1]
            else:
                sum1 += player1[0] + player1[1]
            
        for pin in range(2 , len(player2)):
            if player2[pin-1] == 10 or player2[pin-2] == 10:
                sum2 += (2 * player2[pin])
            else:
                sum2 += (player2[pin])

        if player2[0] == 10:
            sum2 += player2[0] + 2 * player2[1]
        else:
            sum2 += player2[0] + player2[1]

        for pin in range(2 , len(player1)):
            if player1[pin-1] == 10 or player1[pin-2] == 10:
                sum1 += (2 * player1[pin])
            else:
                sum1 += (player1[pin])

        if player1[0] == 10:
            sum1 += player1[0] + 2 * player1[1]
        else:
            sum1 += player1[0] + player1[1]
            
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return 2
        else:
            return 0
