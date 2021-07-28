class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row,col,box =set(),set(),set()
        # row, column, 3*3의 box에 중복되는 숫자가 있는지 확인하기 위해 중복되는 수는 하나로 표시해주는 set함수를 사용한다.
        for i in range(9):
            for j in range(9):
                #만약 board에 .이 없을 때 조건문이 실행된다.
                if board[i][j]!='.':
                    # r,c,b에 각각 r은 row의 번호와 해당 숫자
                    r=(i,board[i][j])
                    # column은 col의 번호와 해당숫자
                    c=(j,board[i][j])
                    # 박스의 크기가 3*3이기 때문에 3보다 큰 수가 row나 col방향으로 들어가면 안되기 때문에 
                    b=(i//3,j//3,board[i][j])
                    #마지막으로 r,c,b가 각각 row, col, box에 있다면 False를 반환
                    if r in row or c in col or b in box:
                        return False
                    row.add(r)
                    col.add(c)
                    box.add(b)
        return True
