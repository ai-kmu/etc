# 정답 봤습니다..
# BFS를 이용한 풀이

from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        # 최악의 경우의 수는 10000(1이 10000번)
        answer = 10000
        q = deque()
        # 초기 q의 상태는 n 그대로와 count가 0임
        q.append((n, 0))
        # 방문 여부 확인
        visited = set()

        while q:
            num, count = q.popleft()
            # 가장 빨리 0에 도달한 count가 최소 count
            # answer = min(answer, count)를 사용하면 time limit
            if num == 0:
                return count
            i = 1
            # i를 증가시키면서 i의 제곱수를 num에서 뺐을 때 나머지와 count를 큐에 추가
            # res에 도달했으면 방문처리
            while i ** 2 <= num:
                res = num - (i ** 2)
                if res not in visited:
                    q.append((res, count + 1))
                    visited.add(res)
                i += 1
