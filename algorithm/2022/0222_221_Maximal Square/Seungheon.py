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
