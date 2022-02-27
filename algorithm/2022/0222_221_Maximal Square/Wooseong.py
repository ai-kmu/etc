class Solution:
    def maximalSquare(self, matrix):
        # matrix size 측정
        m = len(matrix)
        n = len(matrix[0])

        # int로 변환
        matrix = [[int(matrix[i][j]) for j in range(n)]
                                     for i in range(m)]

        # 행이나 열이 1개인경우
        # 1이 하나라도 있다면 답은 1
        # 1이 없다면 0
        if (m == 1) or (n == 1):
            for i in matrix:
                if sum(i): return 1 # 한 행의 합이 1이상이면 1이 하나라도 있는 것 (true)
            return 0

        # Possible Kernel Length (pkl) = 행,열 중 작은 값
        # 작은 값이 1인 경우는 위에서 처리 완료
        pkl = range(min(m,n),1,-1)
        for s in pkl:
            flag = 0

            # 커널 column의 시작점
            for s_col in range(0, n-s + 1):
                # 커널 row의 시작점
                for s_row in range(0, m-s + 1):
                    # 커널 사이즈, s개의 row에 대해 분석
                    for nth_row in range(0, s):
                        row = s_row + nth_row
                        linear_kernel = matrix[row][s_col:s_col+s] # 해당 행 복사
                        linear_sum = sum(linear_kernel)
                        if linear_sum == s: # 해당 행의 합이 s면 == 모두 1이면
                            flag += 1 # 계속
                            if flag == s: # s 개의 행에 대해 통과하면
                                return s**2 # 답
                        else: # 모두 1이 아니면 
                            flag = 0 # 다음 행부터 커널 처음 시작
                            break                            
        return 0
