class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
      
        if maxMove == 0: return 0
        dpCurr = [[0] * (n+2) for _ in range(m+2)]
        dpLast = [[0] * (n+2) for _ in range(m+2)]
        
        return ans
