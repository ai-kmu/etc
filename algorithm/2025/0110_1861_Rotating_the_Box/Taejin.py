class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # 새로 저장할 90도 뒤집힌 행렬 선언
        newBoxGrid = [[0] * len(boxGrid) for _ in range(len(boxGrid[0]))]

        for r in range(len(boxGrid)):
            # *는 벽이므로 *로 구역을 나누어 정렬
            grid = "".join(boxGrid[r]).split("*")
            new_grid = []

            # *를 기준으로 나누어진 구역별로 정렬(중력 적용)
            for g in grid:
                new_grid.append("".join(sorted(g, reverse=True)))
            
            # 합치기
            boxGrid[r] = list("*".join(new_grid))

            # 90도 뒤집은 배열에 저장
            for c in range(len(boxGrid[0])):
                newBoxGrid[c][-(r + 1)] = boxGrid[r][c]

        return newBoxGrid
