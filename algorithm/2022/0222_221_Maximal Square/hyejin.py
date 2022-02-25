class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # binary matrix
        # 1만 있는 가장 큰 square를 찾아라
        m, n = len(matrix), len(matrix[0])
        # convert to integer
        matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        answer = 0
        
        # 완전탐색은 시간이 오래걸림
        
        # matrix에서 0번쨰 컬럼과 0번째 row에 1이 있는지 없는지 먼저 검사
        for i in range(m):
            answer = max(answer, matrix[i][0])
        for i in range(n):
            answer = max(answer, matrix[0][i])

        # 이전 위치가 1일 때, 최대 길이가 담길 수 있게 dp 사용
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]: # 1이면 어디까지 가능한지 체크해야함
                    # 가로기준 이전과 세로기준 이전이 1이라면 비교하여 min인 것을 선택하고 + 1
                    # 대각선이 0이면 사각형이 되지 않으므로 대각선도 체크=> 0이어야함
                    # 그값이 (i,j)에서의 최대 길이
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    answer = max(answer, matrix[i][j])
                    
        return answer ** 2
