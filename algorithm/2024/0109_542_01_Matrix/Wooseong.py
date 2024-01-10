class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        # top down DP
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]:
                    top = mat[r - 1][c] if r else float('inf')
                    left = mat[r][c - 1] if c else float('inf')
                    mat[r][c] = min(top, left) + 1  # top이나 left에서 한 칸

        # bottom up DP
        for r in range(rows - 1, -1, -1):
            for c in range(cols -1, -1, -1):
                if mat[r][c]:
                    bot = mat[r + 1][c] if r < rows - 1 else float('inf')
                    right = mat[r][c + 1] if c < cols -1 else float('inf')
                    near = min(bot, right) + 1  # bot이나 right에서 한 칸
                    mat[r][c] = min(near, mat[r][c])  # top down DP하면서 업데이트 된 게 더 가까울 수도 있음

        return mat  
