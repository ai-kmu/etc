## 풀이 방법
## 1. 주어진 행렬[i][j] 1인지 확인 => 1일 경우 1 * 1 사이즈(최소) 정사각형 생성 가능
## 2. 주변 값들 ([i-1][j], [i][j-1], [i-1][j-1]) 에서 값들 중 작은 값에 1을 더함
## 3. 결과값 중 가장 큰 값(가장 큰 정사각형의 한 변의 길이)를 지속적 갱신

class Solution:
    def maximalSquare(self, matrix):
        
        
        ## 1. 필요한 변수 정의
        row, col = len(matrix), len(matrix[0])        # 입력 행렬의 행, 열 개수 할당(반복문 + 결과 행렬 생성)
        value = 0                                     # 가장 큰 정사각형 한 변의 길이(최초 할당: 0)
        result = [[0] * (col)  for i in range(row )] # 결과 행렬

        # 반복문
        for i in range(row):
            for j in range(col):

                ## 첫번째 행, 열의 경우: 주변 값들([i-1][j], [i][j-1], [i-1][j-1])를 확인할 수 없으므로 주어진 인자가 1 여부만 확인
                if i == 0 or j == 0:
                    result[i][j] = [1 if matrix[i][j] == "1" else 0][0] 
                    
                ## 이외의 요소들의 경우: 주어진 위치가 1이면 주변 값(생성 가능한 정사각형의 한변의 길이)들의 값을 비교해 
                ## 최소값을 할당
                else:
                    result[i][j] = [min(result[i-1][j-1], result[i][j-1], result[i-1][j]) + 1 if matrix[i][j] == "1" else 0][0]
                    
                ## 결과값을 비교해 가장 큰 값을 저장
                value = max(value, result[i][j])
                
        return value ** 2 # 정답의 경우 정사각형의 넓이 => 최대 정사각형의 길이의 제곱으로 결과 도출
