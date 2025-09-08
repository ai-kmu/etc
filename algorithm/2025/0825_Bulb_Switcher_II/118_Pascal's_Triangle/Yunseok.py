class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle_list = [[1]]

        for i in range(1, numRows):
            prev_row = pascals_triangle_list[-1]
            current_row = [1]

            print('current_i: ', i)
            for j in range(len(prev_row) - 1):
                print(j)
                current_row.append(prev_row[j] + prev_row[j+1])

            current_row.append(1)
            pascals_triangle_list.append(current_row)

        return pascals_triangle_list
