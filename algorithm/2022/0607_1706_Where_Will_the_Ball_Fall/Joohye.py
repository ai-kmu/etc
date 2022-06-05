class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        # grid의 길이
        m = len(grid)
        # grid에서 0번째에 들어있는 요소의 개수
        n = len(grid[0]) 
        
        #정답값 -1로 초기화
        answer = [-1]*n 
        
        # for문으로 하나씩 탐색해가면서 풀기
        for j in range(n): 
            # j값을 g1에 따로 저장해서 사용
            g1 = j
            for i in range(m):
                g2 = g1 + grid[i][g1]
                # 만약 g2가 n보다 크거나, 0보다 작은경우 = 공이 못내려감
                if not 0 <= g2 < n :
                    break
                # grid에서 1과 -1이 만났을 경우 = 음수 = 공이 못내려감
                elif grid[i][g1] * grid[i][g2] < 0: 
                    break
                g1 = g2 
                
            # break문에 한번도 걸리지 않은 경우
            else: answer[j] = g1 
        return answer
