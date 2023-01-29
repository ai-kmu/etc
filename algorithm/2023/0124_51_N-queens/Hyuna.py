class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        # 각 행의 퀸의 위치(column) 저장하는 배열 - 0번 행에 2번째 인덱스에 퀸이 있다면 col[0] = 2 
        col = [0] * n

        # 더 진행해도 되는지 확인하기 위한 함수 
        def isOk(row):
            i = 0
            isOk = True

            while (i<row and isOk):
                # 같은 열에 있거나 대각선에 있을 때는 진행하면 안되기 때문에 isOk = False
                if col[row] == col[i] or abs(col[row]-col[i]) == (row-i):
                    isOk = False
                    break

                i += 1
            
            return isOk
        
        def nQueens(row):
            # 진행해도 되는지를 확인  
            if isOk(row):
                # 모든 행마다 퀸을 놓았을 경우 답에 추가시켜줌 
                if (row == n-1):
                    ans.append(formAns(col))
                # 마지막 행이 아닌 경우 
                else:
                    for i in range(n):
                        col[row+1] = i
                        # 그 다음 행을 봄 
                        nQueens(row+1)

        # 답에 추가시킬 때 문제에서 요구하는 스트링 형식에 맞춰주는 함수 
        def formAns(col):
            temp = []
            
            for q in col:
                string = '.' * n
                string = string[:q] + 'Q' + string[q+1:]
                temp.append(string)
            return temp 

        # 한 행에 각각의 열에 퀸을 놓아봄 
        for i in range(n):
            col[0] = i
            nQueens(0)
        
        return ans
