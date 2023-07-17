# 한 조각을 맞추지 못해서 못 풀었습니다.
# 솔루션

class Solution:
    def containsCycle(self, A: List[List[str]]) -> bool:
        R, C = len(A), len(A[0])
        visited = set()
        
        def neighbors(r, c):
            return [(i, j) for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if 0 <= i < R and 0 <= j < C and A[i][j] == A[r][c]]
        
        def dfs(r, c, x, prev, seen):
            if (r, c) in seen:
                return True
            seen.add((r, c))
            visited.add((r, c))

            for i, j in neighbors(r, c):
                if not prev or prev != (i, j):
                    if dfs(i, j, x, (r, c), seen):
                        return True
            return False
            
        
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited:
                    seen = set()
                    if dfs(r, c, A[r][c], None, seen):
                        return True
        return False
