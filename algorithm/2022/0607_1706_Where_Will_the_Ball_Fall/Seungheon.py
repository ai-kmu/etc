class Solution(object):
    def findBall(self, grid):
        
        # '왼', '오' 는 공이 어느방향으로 향하는지 이다
        # 반환값은 막혔으면 -1, 막히지 않았으면 현재 위치이다
        
        def nextPath(i,j):
            # 우단
            if len(grid[0])-1 == j:
                # 오
                if grid[i][j] == 1:
                    return -1
                # 왼
                else:
                    # 오
                    if grid[i][j-1] == 1:
                        return -1
                    else:
                        return j-1
            # 좌단
            elif j == 0:
                # 오
                if grid[i][j] == 1:
                    # 오
                    if grid[i][j+1] == 1:
                        return j+1
                    else:
                        return -1
                # 왼
                else:
                    return -1
            # 가운데
            else:
                # 오
                if grid[i][j] == 1:
                    # 왼
                    if grid[i][j+1] == -1:
                        return -1
                    # 오
                    else:
                        return j+1
                # 왼
                else:
                    # 왼
                    if grid[i][j-1] == -1:
                        return j-1
                    # 오
                    else:
                        return -1
                    
        answer = []
        for j in range(len(grid[0])):
            in_j = j
            i = 0
            
            # 맨 아래 도달할때까지 반복
            while i != len(grid) :
                in_j = nextPath(i, in_j)
                i += 1
                # 막히면 종료
                if in_j == -1:
                    answer.append(-1)
                    break
            # 값 확인        
            if in_j != -1:
                answer.append(in_j)
                
        return answer
