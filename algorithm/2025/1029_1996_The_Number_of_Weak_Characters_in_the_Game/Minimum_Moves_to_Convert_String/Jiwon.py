class Solution:
    def minimumMoves(self, s: str) -> int:
        if "X" not in s:
            return 0
        
        moves = 0
        skip = 0

        for ch in s:
            if skip > 0:
                skip -= 1
                continue

            if ch == 'X':
                moves += 1
                skip = 2

        return moves
