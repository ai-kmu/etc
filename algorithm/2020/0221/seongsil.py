from collections import deque

def bfs():
    time[init] = 0
    q = deque([init])
    while q:
        v = q.popleft()
        next_ = [v-1, v+1, v*2]
        for next_step in next_:
            if 0 <= next_step < MAX and time[next_step]==-1:
                if i == v*2:
                    q.appendleft(next_step)
                    time[next_step] = time[v]
                else:
                    q.append(next_step)
                    time[next_step] = time[v] + 1
    return time[final]

MAX = 100001
init, final = map(int, input().split())
time = [-1] * MAX
print(bfs())
