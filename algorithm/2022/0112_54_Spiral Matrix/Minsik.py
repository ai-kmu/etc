class Solution:
    def spiralOrder(self, matrix):    
        m = len(matrix)    
        n = len(matrix[0]) 
        i, j = 0, 0        

        spiral = []        # spiral metrix를 저장할 list 정의 


        while i < m and j < n:
            # 좌상단 -> 우상단의 값(윗선)
            for up_side in range(j, n):
                spiral.append(matrix[i][up_side])

            i = i + 1   # 내부 직사각형을 그리기 위한 변환
            
            # 우상단 -> 우하단 값(오른쪽 선)
            for right_side in range(i, m):
                spiral.append(matrix[right_side][n-1])
                
            n = n - 1   # 내부 직사각형을 그리기 위한 변환
            
            #if문이 없으면 -> while에서 or의 경우가 반복되어서 잘뭇된 결과가 나옴
            
            # 우하단 -> 좌하단 값(아래선) 
            if i < m: 
                for under_side in range(n-1, j-1, - 1):
                     spiral.append(matrix[m-1][under_side])

                m = m - 1 # 내부 직사각형을 그리기 위한 변환

            # 좌하단 -> 우상단 값(왼쪽 선)
            if j < n:
                for left_side in range(m-1, i-1, -1):
                    spiral.append(matrix[left_side][j]) 

                j = j + 1  # 내부 직사각형을 그리긱 위한 변환
            
        return spiral
