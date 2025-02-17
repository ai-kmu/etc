class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        i, j = 0, 0  # two pointer
        ans = list()  # 정답 저장
        visited = [[False] * col for _ in range(row)]  # 이미 방문한 index 저장
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 방향 저장
        direction_order = 0  # 현재 진행할 방향
        cnt = 0  # 방문한 index 수 저장
        while cnt != row * col:
            while True:
                ans.append(matrix[i][j])
                visited[i][j] = True 
                cnt += 1  
                i += direction[direction_order][0]  # 방향대로 update
                j += direction[direction_order][1]  # 방향대로 update
                if i >= row or j >= col or i < 0 or j < 0 or visited[i][j]:  # 제공된 matrix 범위를 벗어나거나 이미 방문한 index라면 반복문 탈출
                    i -= direction[direction_order][0]  # index 복구
                    j -= direction[direction_order][1]  # index 복구
                    direction_order += 1  # 방향 전환
                    if direction_order == len(direction):
                        direction_order = 0
                    i += direction[direction_order][0]  # 새로운 방향으로 update
                    j += direction[direction_order][1]  # 새로운 방향으로 update
                    break
        return ans
