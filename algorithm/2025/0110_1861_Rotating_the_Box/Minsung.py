from collections import deque

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row, col = len(boxGrid), len(boxGrid[0])
        
        # Step 1 : Rotate boxGrid -> rotatedGrid
        rotatedGrid = [[] for _ in range(col)]
        for j in range(col):
            for i in list(range(row))[::-1]:
                rotatedGrid[j].append(boxGrid[i][j])

        # Step 2 : Applying Gravity
        row, col = len(rotatedGrid), len(rotatedGrid[0])
        for j in range(col):  # 각 column 별로 gravity 적용
            cur_col = ""  # 현재 다룰 column
            tmp = deque()
            '''
            stone -> tmp right에 위치
            empty -> tmp left에 위치 (이로인해 stone은 empty보다 right에 위치)
            obstacle -> gravity의 영향을 받지 않으므로 tmp 정보 저장 후 초기화
            '''
            for i in range(row):
                if rotatedGrid[i][j] == '#':
                    tmp.append(rotatedGrid[i][j])
                elif rotatedGrid[i][j] == '.':
                    tmp.appendleft(rotatedGrid[i][j])
                elif rotatedGrid[i][j] == '*':
                    # tmp 정보 저장 후 초기화
                    cur_col += ''.join(tmp) + '*'  
                    tmp = deque()
                else: raise ValueException 
            cur_col += ''.join(tmp)
            for i in range(row):  # graivity를 고려한 현재 column 저장
                rotatedGrid[i][j]=cur_col[i]
            
        return rotatedGrid
