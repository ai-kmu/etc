class Solution:
    def printVertically(self, s: str) -> List[str]:
        grid = [list(sub_s) for sub_s in s.split()]
        length = len(max(s.split(), key=lambda x:len(x)))
        new_grid = ["" for _ in range(length)]

        for r in range(len(grid)):
            for c in range(length):
                if c < len(grid[r]):
                    new_grid[c] += grid[r][c]

                else:
                    new_grid[c] += " "

        for c in range(length):
            new_grid[c] = new_grid[c].rstrip()
        
        return new_grid
