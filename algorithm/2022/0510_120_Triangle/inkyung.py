class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp문제
        # 거꾸로 밑에서 위로 올라가면서 i 번째 값과 i + 1 번째 값을 비교하고 그 중 작은걸 더해감
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]
