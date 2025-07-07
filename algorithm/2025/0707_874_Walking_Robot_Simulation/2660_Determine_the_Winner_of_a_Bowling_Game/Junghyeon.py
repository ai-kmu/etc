# 하드코딩

class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        def get_score(score):
            s = 0
            for idx, i in enumerate(score):
                if idx == 1:
                   if score[0] == 10:
                    i = 2 * i 
                if idx - 2 >= 0:
                    if score[idx-1] == 10 or score[idx-2] == 10:
                        i = 2 * i

                s += i  

            return s

        p1 = get_score(player1)
        p2 = get_score(player2)

        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0
