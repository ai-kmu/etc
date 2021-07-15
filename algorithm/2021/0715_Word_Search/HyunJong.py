##실패
import numpy as np
class Solution(object):
    def exist(self, board, word):
        cols, rows =np.shape(board)
        list_str = list(word)
        first = list_str.pop(0)
        stack = []
        qu = []
        for i in range(cols):
            for j in range(rows):
                if first == board[i][j]:
                    stack.append((i, j)) 
        for i in stack:
            qu.append(i)  
        if (0 == len(qu)):
            return False            
        if (len(qu) == (len(list_str)+1)):
            return True
        count = 0
        for check, str in enumerate(list_str): ## 이번에 원하는 곳
            new_stack = []
            for stack_num in stack: ##현재 위치에서 시작
                a, b= stack_num ## 현재위치
                a_bf = a - 1 ## 상하좌우 위치
                b_bf = b - 1
                a_af = a + 1
                b_af = b + 1
    
                pos = [(a, b_bf), (a, b_af), (a_bf,b), (a_af, b)] ##left, right, up, down ## 상하좌우 위치 저장
                for i in pos: ## 갈 수 있는지 탐방 시작
                    x, y = i
                    if i not in qu and x>=0 and y>=0 and x<cols and y < rows: ##가본적 없고, x,y가 범위안에 있을 때
                        if (str == board[x][y]): ## 만약 원하는 위치가 있으면 
                            new_stack.append((x, y)) ## 새로운 스택에 넣는다.
                            qu.append((x, y)) ## 가본 적 있기 때문에 qu에 넣는다.
            if (len(new_stack) != 0):
                count+=1
            stack = new_stack
        
        if (count+1 == len(list_str)+1):
            return True
        else:
            return False
