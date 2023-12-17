class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.answer = False
        n, m = len(board[0]), len(board)
        # 방문 확인을 위한 board와 같은 크기의 배열 visited 선언
        visited = [[False] * n for _ in range(m)]
        # 다음 letter로 움직일 수 있는 범위 설정
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # 백트래킹
        def back(x, y, idx):
            # word를 전부 순회했다면 True
            if idx == len(word):
                self.answer = True
                return
            # 상하좌우로 움직임을 for문으로 확인
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                # 다음 움직이는 곳이 가능한 범위를 벗어나는지 확인
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                # 이미 방문한 곳이 아닌지 확인
                if visited[nx][ny] == True:
                    continue
                # 위의 두 조건을 만족하면서 다음 word와 일치한다면 계속 탐색
                if board[nx][ny] == word[idx]:
                    visited[nx][ny] = True
                    back(nx, ny, idx + 1)
                    visited[nx][ny] = False

        # 맨 처음 일치하는 letter를 찾기 위해 완전탐색
        for i in range(m):
            for j in range(n):
                # 첫 letter를 찾았으면 백트래킹 시작
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    back(i, j, 1)
                    visited[i][j] = False
        return self.answer
