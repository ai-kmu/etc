from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rs, cs = len(mat), len(mat[0])
        matrix = [[0 for _ in range(cs)] for _ in range(rs)]
        visited = [[False for _ in range(cs)] for _ in range(rs)]
        q = deque()
        
        for r in range(rs):
            for c in range(cs):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    visited[r][c]= True
        
        while q:
            row, col, dist = q.popleft()
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                r, c = row + x, col + y
                if r in range(rs) and c in range(cs) and not visited[r][c]:
                    matrix[r][c] = dist + 1
                    q.append((r, c, dist + 1))
                    visited[r][c] = True
                    
        return matrix
