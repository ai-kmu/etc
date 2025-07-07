class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def scoring(player):
            if len(player) <= 1:
                return player[0]
            
            elif len(player) == 2:
                score = sum(player)

                if player[0] == 10:
                    score += player[1]

                return score

            else:
                score = player[-1] + scoring(player[:-1])

                if player[-2] == 10 or player[-3] == 10:
                    score += player[-1]
                
                return score

        p1_score = scoring(player1)
        p2_score = scoring(player2)

        return 1 if p1_score > p2_score else (2 if p1_score < p2_score else 0)



        
