import collections 
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        ans, height, width = 0, len(matrix), len(matrix[0])
        b = [[0] * width]
        for i in range(height):
            new_row = []
            for j in range(width):
                new_row.append(b[i][j] + matrix[i][j])
            b.append(new_row)
        #print(b)        
        for start in range(height):
            for end in range(start, height):
                seen = collections.Counter()
                seen[0] = 1
                tot = 0
                #print(seen)
                for j in range(width):
                    print(b[end+1][j])
                    print(b[start][j])
                    tot += b[end + 1][j] - b[start][j]
                    print("tot", tot)
                    if tot - target in seen:
                        ans += seen[tot - target]
                    seen[tot] += 1
                    #print("seen", seen)
                #print("ans", ans)
        return ans
