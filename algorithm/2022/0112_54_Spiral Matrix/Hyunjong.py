# 발표자 comment
# 주석은 밑 말고 위에 달아주세요

class Solution(object):
    def spiralOrder(self, matrix):
      ## 1. 매 매트릭스 값을 관성적으로 방문한다 
      ## 2. 관성적으로 가다가 막힌 경우 방향을 전환해 준다.
      ##         ## 방향을 전환할 때 왼쪽, 아래, 오른쪽, 위 의 반복이다.
      
        result = []
        ## 답 저장용 리스트
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        ## 왼쪽 -> 아래 -> 오른쪽 -> 위 : 순서대로 저장
        
        x = 0 
        y = 0 
        ## 현재 위치
        
        max_x = len(matrix)
        max_y = len(matrix[0])
        ## 최대 위치
      
        pos = 0
        ## dx dy 의 방향 결정, 0이면 왼쪽 1이면 오른쪽...
        
        for k in range(max_x*max_y):
            ## 전체 matrix 탐방
            
            result.append(matrix[x][y])
            ## 현재 matrix 값 저장
            
            matrix[x][y] = 101
            ## 방문 기록 남기기
            
            nx = x + dx[pos]
            ny = y + dy[pos]
            ## 갈 수 있는 곳인지 미리 탐색
            
            if nx > max_x or nx < 0 or ny > max_y or ny < 0 or matrix[(nx%max_x)][(ny%max_y)] == 101:
                ## 메트릭스를 벗어나거나 가본 곳이면 방향을 바꾸기
                pos = (pos+1)%4
                ## 방향 바뀌는 순서가 반복되기 때문
            
            x = x + dx[pos]
            y = y + dy[pos]
            ## 위치 이동
        return result
            
