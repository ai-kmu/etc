class Solution:
    def maxIncreaseKeepingSkyline(self, grid):

        # row/ col 에서의 skyline view 구하기        
        rowMax, colMax = list(map(max, grid)), list(map(max, zip(*grid))) 

        # maximum total sum that the height of the buildings can be increased
        return sum(min(i,j) for i in rowMax for j in colMax) - sum(map(sum,grid))
