# 풀이 안해주셔도 됩니다요...
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        # 1. 방향 그래프 만들기
        for i in range(n):
            xi, yi, ri = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                xj, yj, rj = bombs[j]

                dx = xi - xj
                dy = yi - yj

                if dx * dx + dy * dy <= ri * ri:
                    graph[i].append(j)

        # 2. 각 폭탄을 시작점으로 DFS
        def dfs(node, visited):
            visited.add(node)

            for nxt in graph[node]:
                if nxt not in visited:
                    dfs(nxt, visited)

        answer = 0

        for start in range(n):
            visited = set()
            dfs(start, visited)
            answer = max(answer, len(visited))

        return answer
