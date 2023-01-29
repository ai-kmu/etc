# 못풀어서 정답 보고 풀었습니다 리뷰 안해주셔도 됩니다.

class Solution(object):
    def solveNQueens(self, n):
        # 테이블생성
        board = [['.']*n for i in range(n)]
        ans =[]
        # 대각선 체크
        def issafe(r,c):
            n = len(board)
            for i in range(n):
                # 세로줄 곂치는지
                if board[i][c] == 'Q':
                    return False
                # 왼쪽 대각선
                if  c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                # 오른쪽 대각선
                if  c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True
        # 체크함수
        def solve(r):
            n = len(board)
            # 퀸을 다 올리면 끝
            if r == n:
                ans.append(["".join(i) for i in board])
                return
            # 퀸 체크하고 다음 열로 넘어가기
            for c in range(n):
                if issafe(r,c):
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.'

        solve(0)
        return ans

        
        
