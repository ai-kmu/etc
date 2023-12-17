class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        c = len(board[0])
        r = len(board)
        visited = set()
        def backtracking(i,j,ind):
            # False 출력 경우
            # 1. i,j가 board에서 범위 벗어남
            # 2. ind값이 word의 최대 index보다 커진경우
            # 3. 현재 i,j에 해당되는 board 알파벳과 현재 ind에 해당되는 word 알파벳이 다른경우
            # 4. 이미 (i,j)를 방문한 경우
            if i < 0 or i >= r or j < 0 or j >= c or ind >= len(word) or board[i][j] != word[ind] or (i,j) in visited:
                return False

            # 정답을 찾은 경우 바로 True 출력
            if ind == len(word)-1:
                return True

            # 방문한 곳 기록
            visited.add((i,j))

            # 상하좌우 탐색
            d1 = backtracking(i+1,j,ind+1)
            d2 = backtracking(i-1,j,ind+1)
            d3 = backtracking(i,j+1,ind+1)
            d4 = backtracking(i,j-1,ind+1)

            # backtracking을 위해 현재 위치 제거
            visited.remove((i,j))

            return d1 or d2 or d3 or d4

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0] and backtracking(i,j,0):
                    return True
        
        return False
