from collections import deque

n, k = map(int, input().split())

MAX = 100000
MIN = 0

distances = [-1 for _ in range(100001)]
distances[n] = 0

to_go = deque()
to_go.append(n)

while to_go:
    now = to_go.popleft()
    
    mult = now*2
    if MIN <= mult <= MAX and distances[mult] == -1:
        to_go.appendleft(mult)
        distances[mult] = distances[now]
    
    a_second_later = [now-1, now+1]
    for _next in a_second_later:
        if MIN <= _next <= MAX and distances[_next] == -1:
            to_go.append(_next)
            distances[_next] = distances[now]+1
                    
                    

print(distances[k])
