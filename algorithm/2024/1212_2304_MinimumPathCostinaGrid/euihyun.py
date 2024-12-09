# 다 해봤는데 인덱스 설정이 헷갈려서 마지막에 답 봤어요
# 실패 케이스
class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        
        # grid의 최소값으로 이동 or 이동 비용이 최소로 이동 두가지중 더 적은 값으로 이동 해야됨
        # ex) 0->2 가는게 6 이면  0+2+6 < 0+1+8 이여서 2로 이동해야됨
        # dp 만들어서 두개를 비교하면서 최소로 이동하면 될듯
        # 각각의 moveCost를 어떻게 할당 하는지가 중요(구현의 중요)
        
        n, m = len(grid), len(grid[1])
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = min(grid[0][0] + grid[1][0] + moveCost[grid[0][0]][0], grid[0][0] + grid[1][1] + moveCost[grid[0][0]][1])
        dp[0][1] = min(grid[0][1] + grid[1][0] + moveCost[grid[0][1]][0], grid[0][1] + grid[1][1] + moveCost[grid[0][1]][1])
        print(dp)
        
        
        # 0~3 -> grid 갯수
        for i in range(1,n-1):
            # 0~2 -> 그리드 안의 갯수
            for j in range(m-1):
                for k in range(len(moveCost[0])):
#                     print(i,j,'i,j')
#                     print(dp[i-1][j-1],'?')
#                     1 0 + 2 0 + moveCost[grid[i][j]][k], 
                    dp[i][j] = min(grid[i][j] + grid[i+1][j] + moveCost[grid[i][j]][k], grid[i][j] + grid[i+1][j+1] + moveCost[grid[i][j]][k] , dp[i-1][j-1])
#                     print(moveCost[grid[i][j]][k],'kk')

# 정답 코드,,, 인덱스 생각 다시 해보자,,,
class Solution(object):
    def minPathCost(self, grid, moveCost):
        """
        :type grid: List[List[int]]
        :type moveCost: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])  # 행(row)과 열(column) 크기
        
        # DP 테이블 초기화
        dp = [[float('inf')] * m for _ in range(n)]
        
        # 첫 번째 행의 값을 그대로 DP 테이블에 복사
        for j in range(m):
            dp[0][j] = grid[0][j]
        
        # DP 테이블 갱신
        for i in range(1, n):  # 행을 순회
            for j in range(m):  # 열을 순회
                for k in range(m):  # 이전 행의 모든 열에서 현재 열로 이동
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[grid[i-1][k]][j] + grid[i][j])
        # 마지막 행에서 최소값 반환
        return min(dp[-1])
