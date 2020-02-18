def prob_1697(N, K):
    from collections import deque

    MAX = 100000
    N, K = map(int, input().split())
    q = deque()
    dist = [-1] * MAX * 2
    dist[N] = 0
    q.append(N)

    while True:
        x = q.popleft()
        if x == K:
            print(dist[x])
            break
        for op in (x, 1, -1):
            nx = x + op
            if 0 <= nx < MAX * 2 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
                
def prob_1285(N, K):
    from collections import deque

    MAX = 100000
    N, K = map(int, input().split())
    q = deque()
    dist = [-1] * MAX * 2
    dist[N] = 0
    q.append(N)

    count = 0
    depth_finished = False

    while q:
        x = q.popleft()
        if x == K:
            depth_finished = True
            count += 1

        if not depth_finished:
            for op in (x, 1, -1):
                nx = x + op
                if 0 <= nx < MAX * 2:
                    if dist[nx] == -1:
                        dist[nx] = dist[x] + 1
                    if dist[nx] < dist[x] + 1:
                        continue
                    q.append(nx)

    print(dist[K])
    print(count)
    
def prob_13549(N, K):
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

def prob_13913(N, K):
    from collections import deque

    MAX = 100000
    N, K = map(int, input().split())
    q = deque()
    dist = [-1] * MAX * 2
    dist[N] = 0
    prev_x = [-1] * MAX * 2
    q.append(N)

    while True:
        x = q.popleft()
        if x == K:
            print(dist[K])
            seq = [K]
            px = prev_x[K]
            while px != -1:
                seq.append(px)
                px = prev_x[px]
            seq.reverse()
            print(' '.join(map(str, seq)))
            break
        for op in (x, 1, -1):
            nx = x + op
            if 0 <= nx < MAX * 2 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                prev_x[nx] = x
                q.append(nx)
