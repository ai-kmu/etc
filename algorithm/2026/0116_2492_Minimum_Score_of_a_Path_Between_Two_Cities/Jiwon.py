class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parents = [i for i in range(n+1)]
        ans = float("inf")

        # 루트 찾기
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        # union find
        def union(a, b):
            a = find(a)
            b = find(b)
            if a < b:
                parents[b] = a
            else:
                parents[a] = b

        for a, b, cost in roads:
            union(a, b)

        for a, b, cost in roads:
            if find(n) == find(a):
                ans = min(ans, cost)

        return ans
