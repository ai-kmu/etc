class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        ans = [[1], [1,1]]
        for i in range(2, numRows):
            tmp = [1]
            for x in range(1, len(ans[i-1])):
                tmp.append(ans[i-1][x-1]+ans[i-1][x])
            tmp.append(1)
            ans.append(tmp)
        return ans

