class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # temp metrix 
        temp_mat = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
        
        n = len(matrix)
        # temp matrix로 기존 값 오ᇑ기기
        for r in range(n):
            for c in range(n):
                temp_mat[r][c] = matrix[r][c]
                
        # 규칙 적용하여 matrix 바꾸기
        for r in range(n):
            for c in range(n):
                matrix[c][n-r-1] = temp_mat[r][c]
