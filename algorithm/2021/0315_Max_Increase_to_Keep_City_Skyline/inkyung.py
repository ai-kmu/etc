class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:   
        row,col=[],[]                       # row를 기준으로 가장 큰 값을 저장
        for i in grid:
            row.append(max(i))
        
        for i in range(len(grid[0])):
            maxi=0
            for j in range(len(grid)):
                maxi=max(grid[j][i],maxi)   # col을 기준으로 가장 큰 값을 저장
            col.append(maxi)
            
        answer = 0
        for i in range(len(row)):
            for j in range(len(col)):
                s = min(row[i],col[j])      # row[i]와 col[j]를 비교해서 더 작은 값이 기준이 됨
                # 가장 큰 값을 기준으로 건물을 더 쌓는 것이 아니라 한 숫자를 기준으로 가로, 세로에서 가장 큰 값 중 작은 값을 기준으로 갱신
                # 현재 숫자와 기준 숫자와의 차이를 계속 더해주면 건물을 얼마나 더 쌓아야하는지 알 수 있음
                answer += abs(grid[i][j]-s)
        return answer
