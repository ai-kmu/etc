# 솔루션 봤습니다..!
from collections import deque


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n_row, n_col = len(grid), len(grid[0])

        visited = [[0 for i in range(n_col)] for j in range(n_row)]  # 방문 여부 체크할 리스트

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 시계방향으로 체크
        answer = False  # 리턴할 값

        def dfs(row, col, parent, letter):
            nonlocal answer  # 현재 함수 내에서 상위 함수의 변수 사용
            visited[row][col] = 1  # 방문 여부 체크
            for direction in directions:
                new_row = row + direction[0]  # 새로운 좌표 계산
                new_col = col + direction[1]

                if 0 <= new_row < n_row and 0 <= new_col < n_col:  # 인덱스 오류 방지
                    if grid[new_row][new_col] == letter:  # 문자가 같으면
                        # 만약 사이클 돌고 돌아왔으면 True 리턴
                        if (parent[0] != new_row or parent[1] != new_col) and visited[new_row][new_col] == 1:
                            answer = True
                            return
                        if visited[new_row][new_col] == 0:  # 아직 방문 안했으면
                            dfs(
                                new_row, new_col, [row, col], letter
                            )  # 새로운 row, col 정보를 기준으로 dfs 다시 호출

        for i in range(n_row):
            for j in range(n_col):  # 전체 grid 확인
                if visited[i][j] == 0:  # 아직 방문 안했으면
                    dfs(i, j, [-1, -1], grid[i][j])  # 자신을 부모 노드로 해서 dfs 호출
                    if answer == True:  # 이미 True면 더 확인할 필요 없음
                        return answer

        return answer
