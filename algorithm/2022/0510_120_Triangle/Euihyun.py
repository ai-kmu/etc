
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 삼각형의 왼쪽은 왼쪽을 더하고, 오른쪽은 오른쪽을 더함
        # 그외의 가운데 들은 더 작은 값을 더하고
        # 다 더하면 바닥에 있는 값들중 최소를 리턴
        
        for i in range(1,len(triangle)):
            for j in range(i+1):        
                #맨 왼쪽은 이전행의 왼쪽값 더하기
                if j==0:
                    triangle[i][j]+=triangle[i-1][j]
                
                #맨 오른쪽은 이전행의 맨 오른쪽값 더하기
                elif j==i:
                    triangle[i][j]+=triangle[i-1][-1]
                    
                #나머지 중간 부분은 이전행 비교해서 더 작은값 더하기    
                else:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
        
        # 마지막 바닥에서 제일 작은값 리턴
        return min(triangle[-1])

        
