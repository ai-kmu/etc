class Solution:
    def findDiagonalOrder(self, mat):
        from collections import defaultdict

        if not mat or not mat[0]:
            return []

         diagonals = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i + j].append(mat[i][j])
        
        result = []
        for k in sorted(diagonals.keys()):
            if k % 2 == 0:
                result.extend(diagonals[k][::-1])
            else:
                result.extend(diagonals[k])
        
        return result
