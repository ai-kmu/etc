class Solution:
    # 답지 보고 풀었습니다. 넘기셔도 됩니다.
    def dfs(self, m, n, row, col, move):
        if move < 0:
            return 0
        if row < 0 or col < 0 or row == m or col == n:
            return 1

      # 상하좌우 이동하면서 max move에서 1씩 감소
        if (row, col, move) in self.dp:
            return self.dp[(row, col, move)]
        t = self.dfs(m, n, row-1, col, move-1)
        l = self.dfs(m, n, row, col-1, move-1)
        d = self.dfs(m, n, row+1, col, move-1)
        r = self.dfs(m, n, row, col+1, move-1)
        self.dp[(row, col, move)] = t+l+d+r
        return self.dp[(row, col, move)] % (10**9+7)
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # dp 방식으로 풀이
        self.dp = {} # dp저장
        return self.dfs(m, n, startRow, startColumn, maxMove)
        
