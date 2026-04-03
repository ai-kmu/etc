class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        uc, dc, lc, rc = 0, 0, 0, 0

        for i in moves:
            if i == "U":
                uc += 1
            elif i == "D":
                dc += 1
            elif i == "L":
                lc += 1
            else:
                rc += 1

        if (uc - dc == 0) and (lc - rc == 0):
            return True
        else:
            return False
