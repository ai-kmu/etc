class Solution(object):
    def maximalSquare(self, matrix):
        
        answer = 0
        
        # 첫 행에 1 이있나 확인
        if '1' in matrix[0] :
            answer = 1  
            
        # 첫 열에 1 이있나 확인
        for row in matrix :
            if row[0] == '1' :
                answer = 1      
        
        ''' 
        (feedback)
        행벡터 혹은 열벡터 일 경우 정사각형의 최대 값은 1이고 앞서 첫 행과 열의 존재 여부를 확인해서 바로 return 하는 것은 좋은 생각 / 
        코드가 없어도 돌아가는데 문제가 없어서 생략해도 무방
        '''
        
        # 1행 n 열짜리 matrix면 answer return
        if len(matrix) == 1 :
            return answer

        # n행 1 열짜리 matrix면 answer return
        if len(matrix[0]) == 1 :
            return answer
        
        # 각 위치에서 만들수 있는 최대box_size 를 현재 위치에 업데이트
        # 왼쪽, 왼쪽위, 위쪽 을보고 현재 위치에서 만들 수 있는 최대box_size update
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                '''
                (feedback) 잘 짜셧는데..
                현재 위치의 사각형이 존재하는 것과 상관없이 주변 사각형의 존재를 여부를 탐색하고 현재 위치의 정사각형이 존재할 경우(1) 가질 수 있는 최대 사각형을 계산해서
                존재할 경우 이를 업데이틑 하는 방식 => 현재 위치에서 사각형이 존재하는 여부와 상관없이 연산을 진행해야 하
                '''
                up = int(matrix[row - 1][col])
                left_up = int(matrix[row - 1][col - 1])
                left = int(matrix[row][col - 1])
                # 왼쪽, 왼쪽위, 위쪽의 최솟값보다 1 큰 크기로 최대 box_size 설정
                box_size = min(up, left_up, left) + 1  
                # 현재 위치가 1일때만 update
                if matrix[row][col] == '1' :
                    matrix[row][col] = box_size
                    answer = max(box_size, answer)
                    
        return answer**2
