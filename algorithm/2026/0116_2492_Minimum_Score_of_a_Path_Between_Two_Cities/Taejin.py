class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # n까지의 경로중 최소 -> union find로 parenst list 만들고 n과 같은 부모를 가지는 엣지에서 최솟값 반환
        parents = [i for i in range(n + 1)]
        
        def find(a):
            nonlocal parents
            if parents[a] != a:
                parents[a] = find(parents[a])

            return parents[a]

        def union(a, b):
            nonlocal parents
            p_a = find(a)
            p_b = find(b)

            if p_a <= p_b:
                parents[b] = p_a
            
            else:
                parents[a] = p_b

        for r in roads:
            union(r[0], r[1])

        return min([r[2] for r in roads if find(r[0]) == find(n) or find(r[1]) == find(n)])


        

        
