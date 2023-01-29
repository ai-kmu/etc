class Solution(object):
    def solveNQueens(self, n):
        if n == 1:
            return [["Q"]]
        res = []
        col = [0] * (n+1)

        # 퀸이 대각선 혹은 같은 열에 있는 경우를 체크한다
        # 문제 없을 시 True, 같은 열이나 대각선에 있으면 False
        def check_col_diag(i, col):
            k = 1
            check = True
            while k < i and check:
                # col[i] == col[k] : 같은 열에 있는 경우 -> False
                # abs((col[i] - col[k]) == (i-k)) : 같은 대각선에 있는 경우 -> False
                if col[i] == col[k] or abs((col[i] - col[k])) == (i-k):
                    check = False
                k += 1
            return check
        
        def DFS(i, col):
            if check_col_diag(i, col):
                # 만약 끝까지 모두 탐색이 진행됐다면 
                # 정답이기 때문에 결과에 append
                if i == n:
                    res.append(col[1:n+1])

                # 만약 아직 모든 행을 탐색하지 않았을 경우
                # 다음 행의 모든 열을 탐색
                else:
                    for j in range(1, n+1):
                        col[i+1] = j
                        DFS(i+1, col)
        DFS(0, col)
        return [['.' * (i-1) + 'Q' + '.' * (n-i) for i in j] for j in res]
