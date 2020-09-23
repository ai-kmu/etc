import copy
class Solution(object):
    def rotate(self, matrix):
        length=len(matrix)
        matrix_deepcopy=copy.deepcopy(matrix) # 원본 matrix 대신 바꾸기 위한 matrix 복사본

        #열
        for i in range(length):
            row=[]
            #행
            for j in range(length):
                matrix[i][j]=matrix_deepcopy[length-1-j][i] # 복사본의 열의 값들로 원본 matrix의 행 값들을 바꿈

        return matrix

if __name__ == '__main__':
    s=Solution()
    input=[[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate(input))