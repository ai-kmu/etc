'''
1에서 시작해서 2에서 끝나야 함
-1은 갈 수 없음.
0을 모두 지나치면서 2로 가야한다.
(전체 0의 수)에서 지나간 길은 -1해주면서 마지막에 0 count = 0        
'''
class Solution(object):
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count = 0
        
        # 출발, 도착, 통로
        start, end, empty = self.SearchPoint(grid)       
        self.dfs(start[0], start[1], grid, empty)
        return self.count
        
    # 출발, 도착, 통로 찾기
    def SearchPoint(self, array):
        
        m = len(array)
        n = len(array[0])
        empty_point = 0
        
        # for문을 돌면서 출발, 도착, 통로를 찾는다
        for i in range(m):
            for j in range(n):
                if array[i][j] == 1: 
                    start_point = i, j
                elif array[i][j] == 2:
                    end_point = i, j
                elif array[i][j] == 0:
                    empty_point += 1
                    
        return start_point, end_point, empty_point
    
    # dfs 수행 
    def dfs(self, x, y, grid, e): # 0,0 | 2,2
                
        # 범위를 벗어나면
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        
        # 장애물을 만나면
        if grid[x][y] == -1:
            return
        
        # 모든 경로를 통과하고, end point에 도달했으면 count += 1
        if grid[x][y] == 2:
            # end point에 도달했는데 e가 만족을 안 하면 더 이상 진행 안 하기 위해 return 해야 함
            if e != -1:
                return
            # 모든 조건을 만족하면 count!
            self.count += 1
            return
       
        # 위에서 안 걸리면 통로라는 이야기니깐
        e -= 1
        
        # 현재 방문 처리는 장애물 인덱스로
        grid[x][y] = -1
        
        self.dfs(x+1,y,grid,e)
        self.dfs(x-1,y,grid,e)
        self.dfs(x,y+1,grid,e)
        self.dfs(x,y-1,grid,e)
         
        # 다른 dfs는 방문하지 않았을 수도 있으니 원래 인덱스로
        grid[x][y] = 0
        

        
