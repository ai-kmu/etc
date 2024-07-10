class Solution(object):
    def findDiagonalOrder(self, mat):
        # 예외 처리
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        def dfs(row, col, direction, res):
            if 0 <= row < m and 0 <= col < n:
                res.append(mat[row][col])

                # 위쪽 방향인 경우
                if direction == 1:
                    new_row = row - 1
                    new_col = col + 1
                # 아래쪽 방향인 경우
                else:
                    new_row = row + 1
                    new_col = col - 1
                # 제귀 호출
                dfs(new_row, new_col, direction, res)
                
        # 대각선 개수만큼 반복
        for start in range(m + n - 1):
            # 짝수 방향이면 위쪽
            if start % 2 == 0: 
                # 행 열 범위 밖인 경우 처리
                if start < m:  
                    r = start 
                else:  
                    r = m - 1 
                if start < m:  
                    c = 0 
                else: 
                    c = start - m + 1
                dfs(r, c, 1, result)
            # 홀수 방향이면 아래쪽
            else:  
                # 행 열 범위 밖인 경우 처리
                if start < n: 
                    r = 0  
                else:
                    r = start - n + 1
                if start < n: 
                    c = start 
                else:  
                    c = n - 1 
                dfs(r, c, -1, result)
        return result
