'''
(0, 0) -> (m, n)으로 이동하는 경로가 하나여야 함
DFS로 경로의 경우 탐색 후 1인경우 true 리턴
탐색은 무조건 아래 혹은 오른쪽으로만

grid에 대해 DFS로 경로의 경우의 수를 계산하여 1보다 작은 경우에 true 반환
하지만 예외 케이스가 존재해서 실패...
'''
class Solution:
    def isPossibleToCutPath(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        flag = True
        
        # DFS 함수
        def DFS(i, j, flag):
            global cnt
                
            if flag:
                cnt = 0
                flag = False
            
            if grid[i][j] == 0:
                return False
            
            if i == m-1 and j == n-1:
                cnt += 1
                return True
            
            if 0 <= i < m-1 and 0 <= j < n:
                DFS(i+1, j, flag)
                
            if 0 <= j < n-1 and 0 <= i < m:
                DFS(i, j+1, flag)
                
        DFS(0, 0, flag)
        
        # 총 경우의수가 1보다 작거나 같으면 하나만 값을 변경해도 경로가 없을 것
        # 실패
        if cnt <= 1:
            return True
