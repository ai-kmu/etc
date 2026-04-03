class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move = [0] * 4
        for m in moves:
            if m == 'R':
                move[0] += 1 
            elif m == 'L':
                move[1] += 1
            elif m == 'U':
                move[2] += 1
            elif m == 'D':
                move[3] += 1
        if move[0]-move[1] == 0 and move[2]-move[3] == 0:
            return True
        return False
