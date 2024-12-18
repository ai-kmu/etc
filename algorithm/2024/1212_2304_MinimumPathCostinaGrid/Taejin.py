# 솔루션 참고하였습니다.. 풀이 안해주셔도 됩니다 ㅠ

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        # m: grid의 행(row) 개수
        # n: grid의 열(column) 개수
        m, n = map(len, (grid, grid[0]))

        # 초기 최소 비용 변수 설정
        min_cost = 0

        # 비용을 계산하기 위한 리스트 초기화
        # 첫 번째 행의 값을 초기 비용으로 설정
        cost = [grid[0][:]]

        # 각 행(r)과 그 행의 셀(row)을 반복
        for r, row in enumerate(grid):
            if r > 0:  # 첫 번째 행 이후부터 계산
                cost.append([])  # 현재 행의 비용 리스트를 추가
                for c, cell in enumerate(row):  # 각 열(c)과 그 셀 값(cell)을 반복
                    # 이전 행의 모든 셀(j)에서 현재 셀(c)로 이동하는 최소 비용을 계산
                    # 이전 행의 비용(cost[-2][j]) + 이동 비용(moveCost[i][c])
                    # i는 이전 셀(grid[r - 1][j]) 값
                    cost[-1].append(
                        cell + min(cost[-2][j] + moveCost[i][c] for j, i in enumerate(grid[r - 1]))
                    )

        # 마지막 행의 최소 비용 반환
        return min(cost[-1])
