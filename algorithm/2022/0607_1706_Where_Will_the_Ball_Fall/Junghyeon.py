class Solution:
    '''
    DFS 이용
    '''
    def findBall(self, grid: List[List[int]]) -> List[int]:
      
        # dfs 함수
        def dfs(i, j):
            # 공이 바닥에 도착하면 그때의 col위치 인덱스를 result에 저장
            if i + 1 > len(grid):
                return result.append(j)
                
            # col위치 인덱스가 음수가 된다 -> 도달하지 못했으므로 -1 저장
            if j < 0:         
                return result.append(-1)
            
            else:
                try:
                    # grid에 값이 각각 1, -1일때 조건문 실행
                    if grid[i][j] == -1:
                        if grid[i][j-1] == 1:
                            return result.append(-1) 
                        else:
                            dfs(i+1, j-1)
                    else:
                        if grid[i][j+1] == -1:
                            return result.append(-1)
                        else:
                            dfs(i+1, j+1)
                # outofrange 에러 -> 도달하지 못했으므로 -1 저장
                except:
                    return result.append(-1)
                   
        result = list()
        
        # 공을 굴린다.
        for j in range(len(grid[0])):
            i = 0
            dfs(i, j)
            
        return result
