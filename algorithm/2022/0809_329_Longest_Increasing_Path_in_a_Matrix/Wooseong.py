# min heap
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        
        DP = [[1] * COL for _ in range(ROW)]
        max_len = 1
        
        # (값, 인덱스)를 값 순으로 min heap 생성
        # -> 답을 만드는 경로의 시작점은 작은 값일 것이다
        queue = []
        for i in range(ROW):
            for j in range(COL):
                queue.append((matrix[i][j], i, j))  # -matrix하고
        heapq.heapify(queue)
        
        while queue:
            # 작은 값 위치부터 DP
            _, r, c = heapq.heappop(queue)
            # 해당 위치의 상하좌우가
            for ny, nx in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                # 범위를 벗어나지 않고 더 작은 값이라면
                # 해당 위치의 DP를 update 
                if (0 <= ny < ROW and
                    0 <= nx < COL and
                    matrix[ny][nx] < matrix[r][c]):     # > 로 바꾼 거 시간 비교
                    DP[r][c] = max(DP[r][c], 1 + DP[ny][nx])
            
            # max_len 갱신
            max_len = max(max_len, DP[r][c])
        
        return max_len




# DFS with DP (tabulation)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW = len(matrix)
        COL = len(matrix[0])
        
        DP = {}
        
        def DFS(row, col, prev):
            # 인덱스를 벗어났거나 이전 값보다 작은 값이면 더 이상 못 감
            # 0을 반환해서 해당 case 죽임
            if (row < 0 or row >= ROW or
                col < 0 or col >= COL or
                matrix[row][col] <= prev):
                return 0
            
            # 이미 값을 알고 있으면 불러 오기
            if (row, col) in DP:
                return DP[(row, col)]
            
            # 실제 DFS
            # 더 이상 못 간다는 건 그 값 하나만 경로에 넣는 것이기 때문에
            # length의 초깃값은 1
            length = 1
            length = max(length, 1 + DFS(row + 1, col, matrix[row][col]))
            length = max(length, 1 + DFS(row - 1, col, matrix[row][col]))
            length = max(length, 1 + DFS(row, col + 1, matrix[row][col]))
            length = max(length, 1 + DFS(row, col - 1, matrix[row][col]))
            DP[(row, col)] = length
            
            return length
        
        # 완전탐색
        for r in range(ROW):
            for c in range(COL):
                DFS(r, c, -1)
        
        # DP의 value 중에 max가 답임
        return max(DP.values())
