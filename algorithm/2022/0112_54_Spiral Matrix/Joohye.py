# 발표자 comment
# 사실 이 코드도 굳이 comment가 필요해보이진 않지만
# 굳이 달자면 append 말고 +=을 통해 해결하는것이 나아보입니다.
# value를 하나하나 추가할때에는 append를 쓰는것이 좋으나
# 여러개의 value를 한번에 추가할때에는 list를 만들어 넣어주는것이 좋습니다.

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
