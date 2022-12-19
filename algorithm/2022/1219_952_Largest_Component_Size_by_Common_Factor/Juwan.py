class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        parent = [-1]*100001 # parent node 추적을 하기 위한 List

        def find(x): # union find 방식으로 풀이
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(a, b): # node들의 parent node들을 찾기 위한 함수

            a = find(a)
            b = find(b)

            if a != b:
                parent[b] = a

        for i in nums:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    union(j, i)
                    union(i, i//j)

        cnt = 0
        h_t = {}

        for i in nums:
            a  = find(i)
            cnt = max(cnt, 1 + h_t.get(a, 0))
            h_t[a] = 1 + h_t.get(a, 0)
        return cnt
   
