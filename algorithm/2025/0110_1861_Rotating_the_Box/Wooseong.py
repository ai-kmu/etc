class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # boxGrid: n x m
        # rotated: m x n
        m = len(boxGrid)
        n = len(boxGrid[0])
        
        # 회전시키기
        rotated = [[None for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                rotated[i][j] = boxGrid[m - 1 - j][i]

        # 각 열에 대해, 밑에서부터 끌고 내려오기 (떨구기))
        for j in range(m):
            lowest_empty_row = n - 1
            for i in range(n - 1, -1, -1):
                # 떨구기
                if rotated[i][j] == "#":
                    rotated[i][j] = "."
                    rotated[lowest_empty_row][j] = "#"
                    lowest_empty_row -= 1  # 채웠으니까 올리기
                
                # 현재 행이 장애물이면 `lowest_empty_row`를 현재 행의 위로 설정
                elif rotated[i][j] == "*":
                    lowest_empty_row = i - 1

        return rotated
