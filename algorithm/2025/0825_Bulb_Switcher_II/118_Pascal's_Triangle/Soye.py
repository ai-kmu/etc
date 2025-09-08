class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tmp = [[1]]

        for i in range(1, numRows):
            row = [1] 

            for j in range(i-1):
                row.append(tmp[-1][j] + tmp[-1][j+1])

            row.append(1) 
            tmp.append(row)

        return tmp
