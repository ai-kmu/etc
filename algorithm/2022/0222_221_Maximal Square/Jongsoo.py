class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        maximum = 0
        
        #해당 위치에서 갖을 수 있는 1로된 정사각형의 최대 길이를 저장하기 위한 dp 생성
        #dp의 크기는 입력으로 받는 matrix크기와 동일, 모든 요소를 0으로 초기화
        for i in range(len(matrix)):
            dp.append([])
            for j in range(len(matrix[i])):
                dp[i].append(0)
                
        #matrix 중 요소가 1인 위치에서 자신 포함, 왼쪽, 위, 왼쪽+위에 있는 모든 dp의 요소가 1인경우 해당 위치에서는 2*2의 정사각형을 만들 수 있기 때문에 dp에서는 2를 저장
        #만약 matrix 요소가 1이고 주변의 dp 요소가 모두 2인 경우 이미 2인 위치에서는 2*2의 정사각형을 만들 수 있다는 것
        #따라서 해당 dp에서는 3을 갖음(즉 3*3의 정사각형을 만들 수 있음)
        #예외로 matrix 요소가 1인 위치에서 dp 요소가 왼쪽 = 1, 왼쪽+위 = 2, 위 = 0인 경우에는 1로된 정사각형을 1*1밖에 못만듦(그림을 그려보면 쉽게 알 수 있음)
        #결론적으로 위의 모든 과정들을 해결할 수 있는 dp[row][col] = min(왼쪽,위,왼쪽+위)+1의 식을 사용함
        #이 과정속에서 dp요소 중 가장 큰 값을 저장(정사각형 최대 길이를 저장)
        #row 또는 col이 0인 경우에는 자신의 위치에서 위쪽이나 왼쪽의 dp 정보가 없기 때문에 matrix의 요소를 그대로 가져옴
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row == 0 or col == 0:
                    dp[row][col] = int(matrix[row][col])
                else:
                    if int(matrix[row][col]) == 1:
                        dp[row][col] = min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1
                    else:
                        dp[row][col] = 0
                
                maximum = max(maximum,dp[row][col])
                


        return maximum*maximum
                    
