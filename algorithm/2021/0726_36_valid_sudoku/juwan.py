class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set() # 발견한 요소에 대한 집합
        
        for i in range(9): # 전체 sudoku의 가로 길이
            for j in range(9): # 세로 길이
                if board[i][j] != ".": # 문자열이 "."이면 pass
                    
                    row = "row_"+str(i)+ "_"+ board[i][j] # 해당 row에 대한 유일 키값
                    col = "col_"+str(j)+ "_"+ board[i][j] # 해당 col에 대한 유일 키값
                    sub = "sub_("+str(i//3)+", "+str(j//3)+")_"+board[i][j] # sub sudoku에서의 유일 키값
                    
                    
                    if row in seen or col in seen or sub in seen: # 만약 seen 집합에 중복된 것이 하나라도 있으면 유효하지 않은 sudoku
                        return False
                    
                    seen.add(row) # 검증이되면 각 정보들을 집합에 저장함.
                    seen.add(col)
                    seen.add(sub)
                    
                    
        return True # 검사 완료가 된다면 True 리턴
