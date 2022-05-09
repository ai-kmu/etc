#bottom up 개념은 인터넷을 참고하였음
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        #dp 방식으로 해결
        #맨 밑줄을 제외한 열부터 시작해서 자신의 밑의 줄에서 자신으로 오는 경로에서
        #올 수 있는 가장 작은 값을 선택해서 자신과 더함
        #이런 방식으로 계속 위로 올라가면 결국 맨 위의 값은 가장 작은 경로의 값을 갖게됨
        
         '''
          2                          11
         3 4                        9 10
        6 5 7                      7 6 10 
       4 1 8 3 일때                4 1 8 3 의 결과를 갖음
       
      
        '''
        
        for i in range(len(triangle)-2, -1, - 1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i][j] + triangle[i+1][j], triangle[i][j] + triangle[i+1][j+1])
                
        
        return triangle[0][0]
