class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        answer = [-1] * n
        
        for ball in range(n):
            col = ball
            for row in range(m):
                # 지정한 방향으로 이동
                direction = grid[row][col]
                col += direction
                # 이동할 수 없을 경우 멈춤
                if (not 0 <= col < n) or (grid[row][col] != direction):
                    break
            # 완주했을 경우 해당 col을 기록
            else:
                answer[ball] = col
        
        return answer
