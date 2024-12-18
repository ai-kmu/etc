class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # 그리드의 행(m)과 열(n)의 수를 구함
        prev = grid[0][:]  # 첫 번째 행을 시작으로 최소 비용을 저장할 배열

        for i in range(1, m):  # 두 번째 행부터 마지막 행까지 반복
            curr = [math.inf] * n  # 현재 행의 최소 비용을 저장할 배열 초기화
            for j in range(n):  # 현재 행의 각 열에 대해 반복
                for k in range(n):  # 이전 행의 모든 열과 비교하여 최소 비용 계산
                    curr[j] = min(curr[j], prev[k] + moveCost[grid[i-1][k]][j] + grid[i][j])
            prev = curr  # 현재 행의 최소 비용을 이전 행의 최소 비용으로 업데이트
        
        return min(prev)  # 마지막 행에서의 최소 비용 반환
