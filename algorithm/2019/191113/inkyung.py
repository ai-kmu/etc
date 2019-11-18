import collections 
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        ans, height, width = 0, len(matrix), len(matrix[0])
        extra = [[0] * width]
        for i in range(height):
            new_row = []
            for j in range(width):
                new_row.append(extra[i][j] + matrix[i][j])
            extra.append(new_row)     
        for start in range(height):
            for end in range(start, height):
                seen = collections.Counter()
                seen[0] = 1
                tot = 0
                #print(seen)
                for j in range(width):
                    print(extra[end+1][j])
                    print(extra[start][j])
                    tot += extra[end + 1][j] - extra[start][j]
                    print("tot", tot)
                    if tot - target in seen:
                        ans += seen[tot - target]
                    seen[tot] += 1
                    #print("seen", seen)
                #print("ans", ans)
        return ans
