def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j==0:  # 왼쪽 가장자리는 바로 윗 수가 max
                triangle[i][j] += triangle[i-1][j]
            elif j==i:  # 오른쪽 가장자리 또한 바로 윗 수가 max
                triangle[i][j] += triangle[i-1][j-1]
            else: # 그 외에는 두 윗수중 큰 것 더해감
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
                
    return max(triangle[-1])
            
            
    '''
    시간 초과
    def dfs(x,y,triangle):
    
    if x >= len(triangle):
        return 0
    
    return triangle[x][y] + max(dfs(x+1,y,triangle),dfs(x+1,y+1,triangle))

def solution(triangle):
    answer = dfs(0,0,triangle)

    return answer
    '''
