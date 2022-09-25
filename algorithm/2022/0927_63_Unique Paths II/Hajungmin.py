class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # dp 배열 
        path = [[0 for _ in range(n)] for _ in range(m)]
        
        # 만약 시작점과 끝 점이 1이면 경로가 0이므로 0 반환
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        
        for i in range(m):
            for j in range(n):
                # 처음 0, 0은 1로 초기화
                if i == 0 and j == 0:
                    path[i][j] = 1
                
                # 만약 장애물이 있다면 해당 dp인덱스는 0으로 설정
                elif obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                
                # 일반적인 경우 dp 배열에서 위의 인덱스 값 + 왼쪽 인덱스 값으로 현재 경우의 수 구하기
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]
        
        # dp 배열의 마지막 값 반환
        return path[-1][-1]
