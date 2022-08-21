from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # bfs 방식으로 방문한 곳 확인하며 큐 사용 
        visited = [[0 for i in range(len(maze[0]))] for j in range(len(maze))]
        dq = deque([entrance])
        
        # 상 우 하 좌 
        dX = [-1, 0, 1, 0]
        dY = [0, 1, 0, -1]
        ans = 0
        
        
        while dq:
            now = dq.popleft()
            visited[now[0]][now[1]] = 1
            
            # 상우하좌로 인덱스 값을 변경하여 이동할 수 있는 곳인지 확인
            for i in range(len(dX)):
                tempX = now[0] + dX[i]
                tempY = now[1] + dY[i]
                
                # 인덱스 아웃오브 레인지일 경우 컨티뉴
                if tempX < 0 or tempY < 0 or tempX >= len(maze) or tempY >= len(maze[0]):
                    continue
                
                # 안전한 인덱스 값일 때 템프에 넣어줌
                temp = [tempX, tempY]
                
                # 벽이아니고 방문한 곳이 아닌지 확인 
                if maze[temp[0]][temp[1]] == '.' and not visited[temp[0]][temp[1]]:
                    
                    # 테두리에 위치했을 때 (탈출 가능)
                    if (temp[0] == 0) or (temp[0] == len(maze) - 1) or (temp[1] == 0) or (temp[1] == len(maze[0]) -1):
                        ans += 1
                        return ans
                    
                    # 탈출하지 못했을 경우 방문을 트루로 바꿔주고 다음을 위해 큐에 추가
                    visited[temp[0]][temp[1]] = 1
                    dq.append(temp)
             
            ans += 1
      
        # 탈출 할 방법이 없는 경우
        return -1
    
