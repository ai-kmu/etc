from collections import deque

n, k = map(int, input().split())

MAX = 100000
MIN = 0

distances = [-1 for _ in range(100001)]
distances[n] = 0

to_go = deque([n])

while to_go:
    now = to_go.popleft()
    for _next in [2*now, now+1, now-1]:
        if MIN <= _next <= MAX and distances[_next] == -1:
            if _next == 2*now:
                to_go.appendleft(_next)
                distances[_next] = distances[now]
            else:
                to_go.append(_next)
                distances[_next] = distances[now]+1

print(distances[k])
