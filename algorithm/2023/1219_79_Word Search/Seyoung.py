class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        M = len(board) 
        N = len(board[0])
        W = len(word) #찾을 단어 길이

        def dfs(i, j, w):
          # 단어를 모두 찾은 경우
            if w == W: 
                return True

            if (not 0 <= i < M or
                not 0 <= j < N or
                board[i][j] == '#' or
                board[i][j] != word[w]):
                return False

            curr_letter = board[i][j]
          # 해당 위치를 방문하면 @ 으로 변경
            board[i][j] = '@' 

            top = dfs(i - 1, j, w + 1)
            bottom = dfs(i + 1, j, w + 1)
            left = dfs(i, j - 1, w + 1)
            right = dfs(i, j + 1, w + 1)

            # 현재 위치의 문자를 이전 값으로
            board[i][j] = curr_letter

            # 상하좌우로 찾아서 단어를 찾으면 True 반환
            return top or bottom or left or right

        # 백트래킹으로 단어를 찾을 수 있는지 확인
        for i in range(M):
            for j in range(N):
                if dfs(i, j, 0):
                    return True

        # 단어를 찾지 못하면 False 반환
        return False
