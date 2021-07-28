class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 행, 열, 3x3 박스마다 사용된 숫자를 저장하는 행렬
        used = [[set() for x in range(9)] for y in range(3)]
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                # 만약 .이 아닐 경우
                if col != '.':
                    # 해당 위치에서의 사용불가능한 숫자의 집합
                    used_nums = used[0][i].union(used[1][j]).union(used[2][(i//3)*3+j//3])
                    
                    # 만약 해당 위치에서의 숫자가 사용불가능하면 false를 리턴
                    if col in used_nums:
                        return False
                    
                    # 현재 숫자를 used에 추가
                    used[0][i].add(col)
                    used[1][j].add(col)
                    used[2][(i//3)*3+j//3].add(col)                          
        return True
