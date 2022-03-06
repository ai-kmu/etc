class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        '''
        1011
        1101
        1111 이라 가정 1행 1열부터 하나씩 알아보기 
    
        1다음에 숫자가 1? 1이 아닌 0이다. 그래서 최대 정사각형은 1*1이다. 이걸 돌아가면서 반복. 
        반복되는 부분을 찾아야 한다. 
    
        1011   
        1101     
        1111     
        원소를 하나 고르고 오른쪽 아래 대각선으로 검증하고 오른쪽으로 넘긴다.
        마지막 행마지막 원소는 그냥 1이라고 가정 
        '''
        Row, Col = len(matrix), len(matrix[0])
        cache = {}
    
        #재귀적으로 확인한다.
        def find_square(r, c):
            if r>=Row or c>=Col:
                return 0
        
            if (r, c) not in cache: #행과 열이 cache에 기록되어있지 않은 경우
                down = find_square(r+1, c) #아래를 재귀적으로 확인하면서 누적
                right = find_square(r, c+1) #옆을 재귀적으로 확인하면서 누적
                diag = find_square(r+1, c+1) #오른쪽을 재귀적으로 확인하면서 누적
            
                cache[(r, c)] = 0
                #1이나 0이 있는지 알아보기 
                if matrix[r][c] == "1": #matrix에서 r번째행, c번째 열이 1인 경우
                    cache[(r, c)] = 1 + min(down, right, diag)  #위 아래 하나씩 보기
                
            return cache[(r, c)]
            
            
        find_square(0, 0)
        return max(cache.values())**2
