# 틀렸어요... 정답을 봐버렸습니다. 리뷰 안해주셔도 됩니다.
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        if not mat:
            return mat
        
        rows, cols = len(mat), len(mat[0])
    
        # 결과 초기화
        result = [[-1 for _ in range(cols)] for _ in range(rows)]
        
        # 상, 하, 좌, 우
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # 0부터 시작
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        # BFS 사용하여 거리 계산
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # 새로운 위치가 행렬 범위 내에 있고 아직 방문하지 않았다면
                if 0 <= nr < rows and 0 <= nc < cols and result[nr][nc] == -1:
                    result[nr][nc] = result[row][col] + 1
                    queue.append((nr, nc))
        
        return result
