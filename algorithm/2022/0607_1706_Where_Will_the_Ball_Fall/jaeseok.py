# runtime : 381ms, memory : 14.5MB

class Solution:
    def nextpath(self,answer,grid,m,n):
        # 최종적으로 공이 출구에 도달하면 도달한 시점의 row를 answer에 추가
        if m == len(grid):
            answer.append(n)
        # 0번째 공과 마지막 공이 시작할 때 막혀 있으면 -1을 answer에 추가
        elif (n == 0 and grid[m][n] == -1) or (n == len(grid[0])-1 and grid[m][n] == 1):
            answer.append(-1)
        # 공이 통로에 막히는 경우에는 -1을 answer에 추가
        elif (grid[m][n] == 1 and grid[m][n+1] == -1) or (grid[m][n] == -1 and grid[m][n-1] == 1):
            answer.append(-1)
        # 통로가 \\ 모양일 때 nextpath 함수는 현재 위치에서 row와 col이 1씩 더한 상태에서 진행
        elif grid[m][n] == 1 and grid[m][n+1] == 1:
            self.nextpath(answer,grid,m+1,n+1)
        # 통로가 // 모양일 때 nextpath 함수는 현재 위치에서 row는 1이, col은 -1을 더한 상태에서 진행
        else:
            self.nextpath(answer,grid,m+1,n-1)
        
    def findBall(self, grid: List[List[int]]) -> List[int]:
        answer = []
        # 공의 개수 = column의 개수이므로 공의 개수만큼 반복
        for i in range(len(grid[0])):
            self.nextpath(answer,grid,0,i)
        return answer