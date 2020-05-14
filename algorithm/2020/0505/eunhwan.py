def solution(maps):
    answer = -1
    row, col = len(maps) - 1, len(maps[0]) - 1
    dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    path = [[0, 0, 1]]

    while path:
        x, y, cnt = path.pop(0)
        maps[x][y] = 0
        # BFS
        for dx, dy in dr:
            mx, my = x + dx, y + dy
            if mx == row and my == col:
                answer = cnt + 1
                return answer
            if 0 <= mx <= row and 0 <= my <= col and maps[mx][my] == 1:
                maps[mx][my] = 0
                path.append([mx, my, cnt+1])
    return answer
