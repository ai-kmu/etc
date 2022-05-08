class Solution(object):
    def minimumTotal(self, triangle):
        
        #현재 위치까지의 최솟값을 갱신해 가는 방법
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                
                # layer의 처음부분과 끝부분은 선택사항이 한개밖에 없음으로 끝값을 무조건 더해준다
                if (j == 0):
                    triangle[i][0] += triangle[i-1][0]
                elif (j == len(triangle[i])-1):
                    triangle[i][-1] += triangle[i-1][-1]
                    
                # layer의 중간부분은 선택할 수 있는값중 작은값을 선택한다.
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
                    
        # 마지막layer에서 최솟값 return
        return min(triangle[-1])
