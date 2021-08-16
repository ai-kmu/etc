class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # 1일 때 0과의 거리가 얼마나 되는지
        
        # 최대 거리로 초기화
        dist = [[0 if mat[i][j]==0 else len(mat)+len(mat[0]) for j in range(len(mat[0]))] for i in range(len(mat))]
        
        # 순방향 체크
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if dist[r][c] == 0:
                    continue
                for i, j in [(r-1, c), (r, c-1)]:
                    if 0 <= i < len(mat) and 0<= j < len(mat[0]):
                        dist[r][c] = min(dist[i][j] + 1, dist[r][c])
        
        # 역방향 체크
        for r in range(len(mat)-1, -1 , -1):
            for c in range(len(mat[0])-1, -1, -1):
                for i, j in [(r+1, c), (r, c+1)]:
                    if 0 <= i < len(mat) and 0<= j < len(mat[0]):
                        dist[r][c] = min(dist[i][j] + 1, dist[r][c])
        
        
        
        return dist
