from collections import deque

MAX = 100000
N, K = map(int, input().split())
q = deque()
dist = [-1] * MAX * 2
dist[N] = 0
q.append(N)
solution_second = None

while q:
    x = q.popleft()
    if x == K:
        solution_second = dist[K]
        break

    for op in (x, 1, -1):
        nx = x + op
        if 0 <= nx < MAX * 2 and dist[nx] == -1:
            if op == x:
                dist[nx] = dist[x]
                q.appendleft(nx)
            else:
                dist[nx] = dist[x] + 1
                q.append(nx)


print(solution_second)
