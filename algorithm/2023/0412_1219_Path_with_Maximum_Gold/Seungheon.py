class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
    # 시작위치부터 최대값찾기
        def initialize(i, j):
            visited = [[0 for _ in grid[0]] for _ in grid]
            visited[i][j] = 1
            tmp_gird = copy.deepcopy(grid)
            max_gold = 0
            def explore(i, j, prv_g = 0):
                nonlocal max_gold
                
                tmp = tmp_gird[i][j]
                tmp_gird[i][j] += prv_g

                max_gold = max(max_gold, tmp_gird[i][j])

                for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                    
                    # 범위밖 처리
                    if i+di < 0 or i+di >= len(grid) or j+dj < 0 or j+dj >= len(grid[0]):
                        continue
                    
                    # 방문체크
                    if visited[i+di][j+dj] == 1  :
                        continue 
                    visited[i+di][j+dj] = 1
                
                    # 금이 없으면 안감
                    if tmp_gird[i+di][j+dj] == 0:
                        continue
                    
                    # 백트랙킹
                    tmp = tmp_gird[i+di][j+dj]
                    explore(i+di,j+dj, tmp_gird[i][j])
                    visited[i+di][j+dj] = 0
                    tmp_gird[i+di][j+dj] = tmp
            
            explore(i, j)

            return max_gold 

        answer = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                answer = max(answer, initialize(r,c))

        return answer
        
