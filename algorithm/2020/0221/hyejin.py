# N 수빈, K 동생 위치
N, K = map(int, input().split())
if N >= K:
    print(N-K)
else:
    length = min(100001, K*2+1)
    visit = [0] * length
    count = 0
    q = []

    # 갈 수 있는 n*2를 q안에 처음부터 집어넣기
    if N == 0:
        visit[0] = 1
        q.append(0)
    else:
        now = N
        while now < length:
            visit[now] = 1
            q.append(now)
            now *= 2

    while True:
        if visit[K]:
            break
        nxt = []
        for n in q:
            if n > K:
                if 0 <= n-1 < length and not visit[n-1]:
                    nxt.append(n-1)
                continue
            for j in 1, -1:
                if 0 <= n+j < length and not visit[n+j]:
                    nxt.append(n+j)
        nxt = set(nxt) # 중복제거
        q = []
        for i in nxt:
            if i == 0:
                visit[0] = 1
                q.append(0)
                continue
            now = i
            while True:
                if 0 <= now < length and not visit[now]:
                    visit[now] = 1
                    q.append(now)
                if now > K:
                    break
                now *= 2
        q = list(set(q))
        count += 1
    print(count)