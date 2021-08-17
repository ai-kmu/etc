class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from queue import Queue
        
        m, n, que = len(mat), len(mat[0]), Queue()
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]   
        
        for i in range(m):
            for j in range(n):
                if(mat[i][j] == 0):
                    que.put([i, j])
                else:
                    mat[i][j] = -1
         
        while not que.empty():
            y, x = que.get()
            for dy, dx in dirs:
                if 0<=y+dy<m and 0<=x+dx<n and mat[y+dy][x+dx] == -1:
                    que.put([y+dy, x+dx])
                    mat[y+dy][x+dx] = mat[y][x] + 1
            
        return mat
        
                            
        
