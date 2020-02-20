# 8. 숨바꼭질 3
from collections import deque

N, K = map(int, input().split())
MAX = 100001
distance = [-1] * MAX
distance[N] = 0
q = deque([N])

while q:
    x = q.popleft()
    for nx in [2*x, x+1, x-1]:
        if 0 <= nx < MAX and distance[nx] == -1:
            if nx == 2*x:
                q.appendleft(nx)
                distance[nx] = distance[x]
            else:
                q.append(nx)
                distance[nx] = distance[x] + 1

print(distance[K])
