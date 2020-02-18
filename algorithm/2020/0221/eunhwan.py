from collections import deque

n, k = map(int, input().split())
m = 100001
d = [-1] * m
d[n] = 0  # n 에서 시작하니 0 으로 맞춰야함.
q = deque([n])  # 큐에 [n] 넣어놓고 시작.

while q:
    x = q.popleft()
    if x == k:
        break
    for op in (2 * x, x + 1, x - 1): # 0초와 1초인 케이스로 나뉨.
        if 0 <= op < m and d[op] == -1:
            if op == 2 * x: # 시간 X
                q.appendleft(op)
                d[op] = d[x]
            else: # 1초가 걸리는 케이스
                q.append(op)
                d[op] = d[x] + 1

if n == 5 and k == 17:  # 첫 번째 테스트 케이스
    assert d[k] == 2    # k 번째의 비용은 given truth 와 일치해야함.

print(d[k])
