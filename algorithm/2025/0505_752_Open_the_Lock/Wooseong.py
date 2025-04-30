from collections import deque
from itertools import product

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = tuple(deadends)  # 탐색 O(1)으로

        # 예외 케이스 두 개
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        # BFS
        visited = set(["0000"])
        queue = deque([("0000", 0)])
        while queue:
            node, dist = queue.popleft()
            # 탈출 조건
            if node == target:
                return dist
            # 이웃을 미리 계산해 둘 필요 없음
            for i in range(4):  # 자리마다
                for pm in [-1, 1]:  # 위아래로 딸깍
                    new = str((int(node[i]) + pm) % 10)
                    ngbr = node[:i] + new + node[i + 1:]
                    # deadends에 있으면 안 됨
                    if ngbr in deadends:
                        continue
                    # visited에 없으면 추가하고 queue에 push
                    if ngbr not in visited:
                        visited.add(ngbr)
                        queue.append((ngbr, dist + 1))
        
        # 탈출 못 함 == 불가 => -1 return
        return -1



# 0부터 9, 그리고 index error를 방지하기 위해 0, 9 추가 할당
# 0부터 9를 전구 다섯 개로 표현 -> 네 자리는 전구 20개
# 따라서 일의 자리는 그대로, 십의 자리는 <<5, 백의 자리는 <<10, 천의 자리는 <<15로 표현 가능
N = [0b00000, 0b00001, 0b00011, 0b00111, 0b01111, 0b11111, 0b11110, 0b11100, 0b11000, 0b10000, 0b00000, 0b10000]

# 그래프 사전 할당
G = {}
for a in range(10):
    aa = N[a]<<15
    for b in range(10):
        bb = N[b]<<10
        for c in range(10):
            cc = N[c]<<5
            for d in range(10):
                dd = N[d]
                G[aa + bb + cc + dd] = [
                    (N[a-1]<<15) + bb + cc + dd,  # (a-1)bcd
                    (N[a+1]<<15) + bb + cc + dd,  # (a+1)bcd
                    aa + (N[b-1]<<10) + cc + dd,  # ...
                    aa + (N[b+1]<<10) + cc + dd,
                    aa + bb + (N[c-1]<<5) + dd,
                    aa + bb + (N[c+1]<<5) + dd,
                    aa + bb + cc + N[d-1],
                    aa + bb + cc + N[d+1],        # abc(d+1)
                ]

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 예외 케이스 두 개
        if '0000' == target:
            return 0
        if '0000' in deadends:
            return -1
        
        def encode(code):
            """네 자리 str 숫자를 전구 20개로 인코딩"""
            a, b, c, d = code
            return (N[int(a)]<<15) + (N[int(b)]<<10) + (N[int(c)]<<5) + N[int(d)]
        def dist(a, b):
            """두 이진수 사이의 거리 == 끄고 켜야할 전구 개수 == XOR (^)"""
            # 이 값은 한 번 돌릴 때 바꿀 수 있는 전구 (<= 5)보다 클 수 없으므로 휴리스틱 만족
            return (a^b).bit_count()
        
        # A-star : (지금까지 비용 + 목표까지 남은 비용 추정치)가 작은 길부터 가보기
        # 남은 비용 추정 = heuristic -> `dist`
        s = encode('0000')
        t = encode(target)
        visited = set(map(encode, deadends))  # deadends는 사실 미리 방문한 것과 동일
        visited.add(s)  # 시작 지점도 방문에 넣기
        F = [(dist(s,t), 1, s)]  # step+dis, step+1, code

        while F:
            _, step, code = heappop(F)
            for adj in G[code]:
                if adj in visited:
                    continue
                visited.add(adj)
                d = dist(adj, t)
                if d == 0:
                    # 거리 0 == 도착, 현재 step 반환
                    return step
                heappush(F, (d+step, step+1, adj))

        return -1
