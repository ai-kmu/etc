class Solution:
    
    #위에서 아래로 내려가면서 최단 경로를 찾는 방법
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        #위에서 두번째줄부터 시작
        #윗줄에서 자신의 위치로 내려올 때 올 수 있는 가장 작은 값을 자신과 더함
        #맨 왼쪽과 오른쪽은 올 수 있는 값이 하나이므로 if문으로 처리
        #나머지 경우는 min값을 사용해서 올 수 있는 가장 작은 값을 구함
        #이런식으로 위에서 아래로 나려가면 맨 밑줄의 min값이 최단 경로가 된다.
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1],triangle[i-1][j])
        
        return min(triangle[len(triangle)-1])
