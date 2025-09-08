class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    
        # add_list = []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows >= 3:
            add_list = [[1],[1, 1]]
            
            add = []
            for i in range(2, numRows):
                add.append(1)
                for k in range(len(add_list[i - 1]) - 1):
                    tmp = add_list[i - 1][k] + add_list[i - 1][k+1]
                    add.append(tmp)
                add.append(1)
                add_list.append(add)
                add = []
        return add_list


            


