class Solution:
    # def __init__(self, n):
    #     self.parent = list(range(n))
    #     self.rank = [0] * n
    def __init__(self):
        self.parent = None
        self.rank = None

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

        for road in roads:
            # print(road)
            self.union(road[0], road[1])

        root_city = self.find(1) # 1번 도시

        min_score = float('inf')

        for road in roads:
            if self.find(road[0]) == root_city:
                min_score = min(min_score, road[2])

        return min_score
        
