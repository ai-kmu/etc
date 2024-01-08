from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # 0 인부분으로 부터 거리를 1씩 추가하는 방식
      
        # dp table만들기
        # 0인곳만 0으로 나머지는 inf
        dp = [[0 if mat[i][j] == 0 else float('inf') for j in range(len(mat[0]))] for i in range(len(mat))]
        
        Q = deque([])
        
        # 0인부분  Q에 추가
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if dp[i][j] == 0:
                    Q.append((i, j))

        # BFS탐색
        while Q:
            cur_i, cur_j = Q.popleft()
            for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                # out of range
                if cur_i + di < 0 or cur_j + dj < 0 or cur_i + di >= len(mat) or cur_j + dj >= len(mat[0]):
                    continue
                # 현제 거리보다 큰값이 주위에 존재하면 갱신하기위해 Q에 추가
                if dp[cur_i][cur_j] < dp[cur_i + di][cur_j + dj]:
                    Q.append([cur_i + di, cur_j + dj])
                    dp[cur_i + di][cur_j + dj] = dp[cur_i][cur_j] + 1

        return dp
