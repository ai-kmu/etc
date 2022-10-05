from collections import deque
def solution(maps):
    # dfs
    dq = deque([[0, 0, 1]])
    while dq:
        temp = dq.popleft()
        # 종료 조건
        i, j, k = temp
        if i + 1 == len(maps) and j + 1 == len(maps[0]):
            return k
        # dq에 넣기
        if i > 0 and maps[i - 1][j]:
            dq.append([i - 1, j, k + 1])
            maps[i - 1][j] = 0
        if j > 0 and maps[i][j - 1]:
            dq.append([i,  j - 1, k + 1])
            maps[i][j - 1] = 0
        if i + 1 < len(maps) and maps[i + 1][j]:
            dq.append([i + 1, j, k + 1])
            maps[i + 1][j] = 0
        if j + 1 < len(maps[0]) and maps[i][j + 1]:
            dq.append([i, j + 1, k + 1])
            maps[i][j + 1] = 0
    # 못나감
    if not dq:
        return - 1
