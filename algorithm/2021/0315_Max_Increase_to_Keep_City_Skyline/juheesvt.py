class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        change = 0
        
        # 각 행과 열의 최댓값 저장
        row_skyline = [max(h) for h in grid]
        col_skyline = [max(h) for h in zip(*grid)]
        
        # grid를 하나하나 돌면서, 각 행과 열의 최댓값 중 작은 값을 기준으로 최대로 더할 수 있는 수를 change에다가 
        for i, arr in enumerate(grid):
            for j, h in enumerate(arr):
                
                limit = min (row_skyline[i], col_skyline[j])
                if limit > h:
                    change += (limit-h)
                    
                    
        return change
        
