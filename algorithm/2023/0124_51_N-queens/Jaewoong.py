# 풀이실패..
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 백트래킹으로 퀸이 존재하는 경우가 발견되면 초기화하고 처음으로 돌아감
        def check(ls,new):
            for i in range(len(ls)):
                # 같은 열과 대각선에 존재하지 않는 경우
                if new == ls[i] or (len(ls)-i) == abs(ls[i] - new):
                    return False
            return True

        def dfs(n,ls):
            if len(ls) == n:
                return 
            cnt = 0
            for i in range(n):
                if check(ls,i)==True:
                    cnt += dfs(n, ls+[i])
            

