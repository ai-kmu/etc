from collections import deque

def bfs(candidates, place):
    q = deque()
    q.append(candidates)
    direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[False] * len(place[i]) for i in range(len(place))]

    while q:
        y, x, n = q.popleft()
        visited[y][x] = True
        for dy, dx in direct:
            ny = y + dy
            nx = x + dx
            nn = n + 1
            if (0 <= nx <= 4) and (0 <= ny <= 4) and (place[ny][nx] != "X") and (visited[ny][nx] == False) and (nn <= 2):
                if place[ny][nx] == "O":
                    q.append((ny, nx, nn))
                if place[ny][nx] == "P":
                    return False
    return True

def solution(places):
    answer = []
    for place in places:
        result = 1
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == "P":
                    safeness = bfs((i, j, 0), place)
                    if not safeness:
                        result = 0
        answer.append(result)
    return answer
