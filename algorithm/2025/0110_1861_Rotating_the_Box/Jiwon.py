class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        """
        상자 matrix 90도 시계방향 회전
        돌은 중력 따라 아래로 떨어짐 (장애물 또는 벽을 만날 때까지)
        """

        # 중력 적용 먼저 (회전하고 하면 헷갈리니까...)
        for row in boxGrid:
            # 제일 끝(회전 시 아래 칸)부터 확인하면서 적용
            tmp = len(row) - 1
            for col in range(len(boxGrid[0]) - 1, -1, -1):
                # 돌을 빈칸으로 이동 및 빈칸 인덱스 조절
                if row[col] == "#":
                    row[col] = "."
                    row[tmp] = "#"
                    tmp -= 1
                # 장애물의 경우 그 다음 칸으로 tmp 인덱스 변경
                elif row[col] == "*":
                    tmp = col - 1
                
        # 회전 행렬 만들기
        new_grid = [[" "] * len(boxGrid) for _ in range(len(boxGrid[0]))]
        for row in range(len(boxGrid)):
            for col in range(len(boxGrid[0])):
                new_grid[col][len(boxGrid) - 1 - row] = boxGrid[row][col]

        return new_grid
        
