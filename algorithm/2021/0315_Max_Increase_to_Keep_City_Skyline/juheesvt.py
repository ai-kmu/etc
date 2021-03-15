class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        change = 0
        
        row_skyline = [max(h) for h in grid]
        col_skyline = [max(h) for h in zip(*grid)]
        
        for i, arr in enumerate(grid):
            for j, h in enumerate(arr):
                
                limit = min (row_skyline[i], col_skyline[j])
                if limit > h:
                    change += (limit-h)
                    
                    
        return change
        
