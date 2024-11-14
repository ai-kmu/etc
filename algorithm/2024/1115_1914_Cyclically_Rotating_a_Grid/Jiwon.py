## 솔루션 참고: brute-force

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) # dimensions 

        # 바깥 -> 안 으로 각 층을 돌기
        for r in range(min(m, n)//2): 
            i = j = r
            vals = []
            # 윗변: 왼 -> 오
            for jj in range(j, n-j-1):     vals.append(grid[i][jj])
            # 오른쪽 변: 위 -> 아래
            for ii in range(i, m-i-1):     vals.append(grid[ii][n-j-1])
            # 아랫변: 오 -> 왼
            for jj in range(n-j-1, j, -1): vals.append(grid[m-i-1][jj])
            # 왼쪽 변: 아래 -> 위
            for ii in range(m-i-1, i, -1): vals.append(grid[ii][j])

            # 회전하여 새로운 위치로 이동
            kk = k % len(vals)
            vals = vals[kk:] + vals[:kk]

            # 회전 값 다시 채워넣기
            x = 0  
            for jj in range(j, n-j-1):     grid[i][jj] = vals[x]; x += 1
            for ii in range(i, m-i-1):     grid[ii][n-j-1] = vals[x]; x += 1
            for jj in range(n-j-1, j, -1): grid[m-i-1][jj] = vals[x]; x += 1
            for ii in range(m-i-1, i, -1): grid[ii][j] = vals[x]; x += 1
        return grid
