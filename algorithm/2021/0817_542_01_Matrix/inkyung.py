class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        answer = [[0 for _ in range(cols)] for _ in range(rows)] 
        queue = deque()
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        # 이미 0이면 distance를 구할 필요가 없음 --> visited에 True로 표시
        for row in range(rows):
            for column in range(cols):
                if mat[row][column] == 0: 
                    queue.append((row, column, 0))
                    visited[row][column] = True
           
        while queue:
            row, column, distance = queue.popleft()
            # 상하좌우를 확인하면서 이미 방문한 곳이 아니면서 범위안에 있는지 확인
            for x, y in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r, c = row + x, column + y
                # 이미 방문한곳이 아님 == 이전에 0 이었거나 1인 곳
                if r in range(rows) and c in range(cols) and not visited[r][c]:
                    answer[r][c] = distance+1
                    queue.append((r, c, distance+1))
                    visited[r][c] = True
                    
        return answer
