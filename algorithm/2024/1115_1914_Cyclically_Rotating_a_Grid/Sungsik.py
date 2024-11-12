class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m // 2, n // 2)
        
        for i in range(layers):
            # layer를 하나하나 추가
            layer = []
            for row in range(i, m-i):
                layer.append(grid[row][i])
            for col in range(i+1, n-i):
                layer.append(grid[m-i-1][col])
            for row in range(m-i-2, i-1, -1):
                layer.append(grid[row][n-i-1])
            for col in range(n-i-2, i, -1):
                layer.append(grid[i][col])

            # k만큼 rotate
            tmp_k = k % len(layer)
            layer = layer[-tmp_k:] + layer[:-tmp_k]

            # reassign
            j = 0
            for row in range(i, m-i):
                grid[row][i] = layer[j]
                j += 1
            for col in range(i+1, n-i):
                grid[m-i-1][col] = layer[j]
                j += 1
            for row in range(m-i-2, i-1, -1):
                grid[row][n-i-1] = layer[j]
                j += 1
            for col in range(n-i-2, i, -1):
                grid[i][col] = layer[j]
                j += 1
        
        return grid
    
    
   
