class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        
        def dfs(i,j,word):
            if len(word) == 0: #
                return True
            if (i >= len(board) or i < 0 or j >=len(board[0]) or j < 0): # 좌표의 위치가 board의 범위를 벗어나면 false
                return False
            elif board[i][j] != word[0]: # 탐색 중인 곳이 찾는 문자와 일치하지 않으면 false 
                return False
            else:
                temp = board[i][j] # 현재 탐색 중인 것을 저장하고 
                board[i][j] = "@" # 방문 흔적
                w = word[1:]
                if dfs(i-1,j,w) or dfs(i+1,j,w) or dfs(i,j+1,w) or dfs(i,j-1,w):
                    return True
                else:
                    board[i][j] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,word):
                        return True
                  
        return False
