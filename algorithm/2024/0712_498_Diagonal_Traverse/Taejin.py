class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ret = []
        row = len(mat)
        col = len(mat[0])
        
        for i in range(row + col - 1):
            x = i if i < row else row - 1
            y = i - row + 1 if i >= row else 0
            temp = []

            while 0 <= x < row and 0 <= y < col:
                temp.append(mat[x][y])
                x -= 1
                y += 1

            if i % 2:
                temp = temp[::-1]

            ret += temp

        return ret
