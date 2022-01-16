# 껍질 벗기기
# 나선형 달팽이 껍질 모양 시계방향

class Solution(object):
    def spiralOrder(self, matrix):
        result = [] # 뽑아온 값 저장할 리스트 생성
        
        while matrix: # 매트릭스가 빌 때까지 시행            
            # 위 껍질 벗기기
            result += matrix.pop(0) # 매트릭스 최상단 행을  뽑아낸다 
            
            
            # 오른쪽 껍질 벗기기
            if matrix and matrix[0]: # 매트릭스가 2차원 열이 있을 때 시행
                for i in matrix: # 각 행 불러오기
                    result.append(i.pop()) # 행의 마지막 요소(오른쪽) 뽑아내기
                    
            # 아래 껍질 벗기기
            if matrix: # 매트릭스가 비어있지 않을 때 시행
                result += matrix.pop()[[::-1]] # 매트릭스의 마지막 행을 통째로 뽑아낸 후 역순으로 저장
                
            # 왼쪽 껍질 벗기기
            if matrix and matrix[0]: # 매트릭스가 2차원 열이 있을 때 시행
                for i in matrix[::-1]: # 각 행을 역순으로 불러온다.
                    result.append(i.pop(0)) # 행의 첫 번째 요소(왼쪽) 뽑아내기
                    
                                
        return result

        
