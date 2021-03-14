class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # 각 행의 최댓값과 각 열의 최댓값을 구해서 저장
        row_max = [max(row) for row in grid]
        column_max = [max(column) for column in zip(*grid)]
        
        # 문제를 고려한 새로운 grid에서 기존 grid를 뺀 후 모든 요소에 대해 더한 결과를 출력
        # 이 출력이 빌딩 높이를 증가시킬 수 있는 최대 총합이다.
        return sum((min(row_max[i], column_max[j]) - grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))))
