class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return (moves.count("U") - moves.count("D") == 0) and (moves.count("L") - moves.count("R") == 0)
