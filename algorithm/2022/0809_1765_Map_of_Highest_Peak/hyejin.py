class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # isWater m x n
        # 0: land, 1: water
        # cell의 height는 non-negative
        # water height == 0
        # 두개의 adjacent cell은 적어도 1이어야함
        # maximum height
        # 0 부근은 다 1이어야함 => 물 주변부터 채워나가기
        
        m, n = len(isWater), len(isWater[0])
        
        # queue 초기화
        q = deque([])
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    q.append((r, c))
        
        # answer 초기화 and visit 역할
        answer = [[c-1 for c in row] for row in isWater] 
        
        # bfs 수행
        while q:
            curr_r, curr_c = q.popleft()
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # 4방향 체크
                next_r, next_c = curr_r + i, curr_c + j
                if 0 <= next_r < m and 0 <= next_c < n and answer[next_r][next_c] == -1:
                    answer[next_r][next_c] = answer[curr_r][curr_c] + 1
                    q.append((next_r, next_c))
            
                    
        return answer
