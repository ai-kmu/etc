class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            if matrix:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result
        
#처음 ex) matrix =[[1,2,3],[4,5,6],[7,8,9]] 
#1차 matrix = [[4,5,6],[7,8,9]] // result = [1,2,3]
#2차 matrix = [[4,5],[7,8]] // result = [1,2,3,6,9]
#3차 matrix = [[4,5]] // result = [1,2,3,6,9,8,7]
#4차 matrix = [[5]] // result = [1,2,3,6,9,8,7,4]
#result = [1,2,3,6,9,8,7,4,5]
