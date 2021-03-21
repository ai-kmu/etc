class Solution(object):

    def dfs(self,x,y,grid):

        # 격자 범위 체크 할 것
        # 기저 조건 1: 0의 사방면중 하나라도 격자 범위에서 벗어나면 "섬"이 아님
        if x<0 or y <0 or y>=len(grid) or x>=len(grid[0]):
            return False
        # 기저 조건 2 :
        if grid[y][x] == 1:
            return True
        
        # 무한 재귀 방지,, 0 부분을 체크 햇는데도 아무것도 안해주고 넘어가면 똑같은 패턴이 계속나오니까 무한 재귀가 걸림.. 쥬륵
        grid[y][x] = 1
        
        # 상하좌우가 물인지 아닌지 범위에 벗어낫는지 확인하기 위한 재귀 함수 호출
        status1 = self.dfs(x+1, y, grid)
        status2 = self.dfs(x, y+1, grid)
        status3 = self.dfs(x-1, y, grid)
        status4 = self.dfs(x, y-1, grid)

        return status1 and status2 and status3 and status4

    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                # "0"일 때만 들어가서 섬인지 아닌지 체크하면댐
                if grid[row][col] == 0:
                    if self.dfs(col, row, grid):
                        count += 1
                                
        return count
