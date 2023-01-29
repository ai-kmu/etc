# fail code

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # 
        
        board = [ [0 for _ in range(n)] for _ in range(n)]
        answer = []
        
        def check_q(i, j):
            if board[i][j] == 1:
                return 1
            
            for dy, dx in [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]:
                cur_i = i
                cur_j = j
                while cur_i+dy < n and cur_i+dy >= 0 and cur_j+dx < n and cur_j+dx >= 0:
                    cur_i+=dy
                    cur_j+=dx
                    if board[cur_i][cur_j] == 1:
                        return 1
            return 0

        def make_answer():
            tmp_answer = []
            for i in range(n):
                tmp = ''
                for j in range(n):
                    if board[i][j] == 1:
                        tmp += "Q"
                    else :
                        tmp += "."
#                 print(tmp)
                tmp_answer.append(tmp)
            return tmp_answer

        n_count = 0

        def explore(c_i, c_j):
            nonlocal n_count

#             for i in range(n):
#                 print(board[i])
#             print("------------------------------")
            
            for i in range(c_i, n):
                if 1 in board[i]:
                    continue
                for j in range(n):
                    if i == c_i and j < c_j:
                        continue
                    # 현재 위치에 놓을 수 있는지 확인
                    if check_q(i, j):
                        continue
                    
                    board[i][j] = 1
                    n_count += 1

                    if n_count == n:
                        answer.append(make_answer())
                    else:
                        explore(i,j)
                        
                    board[i][j] = 0
                    n_count -= 1
            
            return

        explore(0,0)

        return answer
