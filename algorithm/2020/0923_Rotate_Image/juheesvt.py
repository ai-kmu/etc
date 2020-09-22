class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        n = len(matrix)
        
        # (i,i) 에 있는 숫자들을 제외하고 (i,j) (j,i) 끼리 자리 바꾸기
        for i in range(n):
            for j in range(i):
                print(matrix[i][j], matrix[j][i])
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print(matrix[i][j], matrix[j][i])
         
        # 각 row에서 각 위치와 반대에(?) 있는 숫자와 바꾸기
        for row in matrix:
            for j in range(int(n/2)):
                print(row)
                print(row[j], row[~j])
                row[j], row[~j] = row[~j], row[j]
                print(row[j], row[~j])

        """        
        
        matrix[:] = zip(*matrix[::-1])
        
        리스트 거꾸로 정렬해서 각 인덱스에 있는 요소값끼리 합쳐서 리스트 다시 생성하는 코드
        
        """
