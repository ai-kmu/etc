class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up, down = 1, 0

        y, x = 0, 0
        m, n = len(mat)-1, len(mat[0])-1

        direction = up
        answer = [mat[y][x]]

        while not (y == m and x == n):
            # 오른쪽 위로 향할 경우
            if direction == up:
                if x == n:
                    y += 1
                    direction = down
                elif y == 0:
                    x += 1
                    direction = down

                else:
                    y -= 1
                    x += 1
            # 왼쪽 아래로 향할 경우
            else:
                if y == m:
                    x += 1
                    direction = up
                elif x == 0:
                    y += 1
                    direction = up
                else:
                    x -= 1
                    y += 1
            answer.append(mat[y][x])
        
        return answer

        
