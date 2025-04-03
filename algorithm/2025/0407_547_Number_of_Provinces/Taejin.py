class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        n_groups = len(parents)

        # union find 사용
        # union 되는 경우에 n_groups - 1
        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
            
            return parents[a]

        def union(a, b):
            nonlocal n_groups
            p_a, p_b = find(a), find(b)
            
            if p_a == p_b:
                return

            else:
                n_groups -= 1
                parents[p_b] = p_a

        # 순회하며 union 진행
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j]:
                    union(i, j)

        return n_groups

