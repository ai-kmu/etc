class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        x, y = 0, 0
        r, c = len(matrix), len(matrix[0])

        while r > 1 and c > 1:
            # 오른쪽 방향
            for _ in range(c - 1):
                ret.append(matrix[x][y])
                y += 1

            # 아래쪽 방향
            for _ in range(r - 1):
                ret.append(matrix[x][y])
                x += 1

            # 왼쪽 방향
            for _ in range(c - 1):
                ret.append(matrix[x][y])
                y -= 1
            
            # 위쪽 방향
            for _ in range(r - 1):
                ret.append(matrix[x][y])
                x -= 1
                
            x += 1 # 껍데기 하나 돌고 나면 x 인덱스 하나 증가
            y += 1 # 껍데기 하나 돌고 나면 y 인덱스 하나 증가
            r -= 2 # 껍데기 하나 돌면 2씩 둘레 줆
            c -= 2 # 껍데기 하나 돌면 2씩 둘레 줆

        # 회전할 껍데기 길이 (r, c)가 1 초과인 경우까지 돌았으니, 마지막 r 또는 c가 1인 경우를 추가
        if r == 1:
            ret += matrix[x][y:y+c]

        elif c == 1:
            ret += [matrix[x+dr][y] for dr in range(r)]

        return ret
            
