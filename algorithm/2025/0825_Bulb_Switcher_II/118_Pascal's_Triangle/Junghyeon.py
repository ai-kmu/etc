class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
            
        triangle = [[1]]
        for i in range(1, numRows):
            new_row = [1]
            for j in range(1, i):
                sum_of_element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                new_row.append(sum_of_element)
            new_row.append(1)
            triangle.append(new_row)
            
        return triangle
